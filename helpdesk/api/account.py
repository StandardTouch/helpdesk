import frappe
from frappe import _
from frappe.auth import LoginManager
from frappe.core.doctype.user.user import test_password_strength

from helpdesk.utils import get_post_login_path

CUSTOMER_ROLE = "HD Customer"
COMMON_EMAIL_DOMAINS = {
    "gmail.com",
    "yahoo.com",
    "hotmail.com",
    "outlook.com",
    "icloud.com",
}


@frappe.whitelist(allow_guest=True)
def register_portal_user(full_name, email, password, company_name=None):
    """Self-service signup for the customer portal.

    Creates a Website User with only the `HD Customer` role, a linked Contact
    (and HD Customer when a company is given), then logs the user in.
    """
    if not full_name or not full_name.strip():
        frappe.throw(_("Full Name is required"))
    if not email or not email.strip():
        frappe.throw(_("Work Email is required"))
    if not password or len(password) < 6:
        frappe.throw(_("Password must be at least 6 characters"))

    email = email.strip().lower()
    frappe.utils.validate_email_address(email, throw=True)

    if frappe.db.exists("User", email):
        frappe.throw(_("An account with this email already exists. Please log in."))

    parts = full_name.strip().split(" ", 1)
    first_name = parts[0]
    last_name = parts[1] if len(parts) > 1 else ""
    company_name = (company_name or "").strip()

    previous_user = frappe.session.user
    frappe.set_user("Administrator")
    try:
        user = frappe.get_doc(
            {
                "doctype": "User",
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "send_welcome_email": 0,
                "user_type": "Website User",
                "roles": [{"role": CUSTOMER_ROLE}],
            }
        )
        user.flags.delay_password_email = True
        user.insert(ignore_permissions=True)

        from frappe.utils.password import update_password

        update_password(user.name, password)

        if company_name and not frappe.db.exists("HD Customer", company_name):
            hd_customer = frappe.new_doc("HD Customer")
            hd_customer.customer_name = company_name
            domain = email.split("@")[1]
            if domain not in COMMON_EMAIL_DOMAINS:
                hd_customer.domain = domain
            hd_customer.insert(ignore_permissions=True)

        contact = _get_or_create_contact(user, first_name, last_name, company_name)
        if company_name and frappe.db.exists("HD Customer", company_name):
            if not any(
                link.link_doctype == "HD Customer" and link.link_name == company_name
                for link in contact.links
            ):
                contact.append(
                    "links", {"link_doctype": "HD Customer", "link_name": company_name}
                )
        if company_name:
            contact.company_name = company_name
        contact.save(ignore_permissions=True)

        frappe.set_user(user.name)
        LoginManager().login_as(user.name)
        frappe.db.commit()

        return {
            "status": "success",
            "message": _("Account created successfully"),
            "user": user.name,
            "full_name": user.full_name or first_name,
            "redirect_to": get_post_login_path(user.name),
        }
    except Exception:
        frappe.db.rollback()
        frappe.set_user(previous_user)
        raise


def _get_or_create_contact(user, first_name, last_name, company_name):
    contact_name = frappe.db.get_value("Contact", {"email_id": user.email})
    if contact_name:
        contact = frappe.get_doc("Contact", contact_name)
    else:
        contact = frappe.new_doc("Contact")
        contact.first_name = first_name
        contact.last_name = last_name
        contact.append("email_ids", {"email_id": user.email, "is_primary": 1})
    contact.user = user.name
    return contact


@frappe.whitelist(allow_guest=True)
def validate_password(password, first_name, last_name, email):
    result = test_password_strength(password, "", None, (first_name, last_name, email))
    feedback = result.get("feedback")
    return not (
        feedback and not feedback.get("password_policy_validation_passed", False)
    )


def on_user_insert(doc, method=None):
    """Website Users created any other way (OAuth, invite, desk) become portal
    customers with a Contact, and never get desk access."""
    if doc.user_type != "Website User":
        return

    if CUSTOMER_ROLE not in [r.role for r in doc.roles]:
        doc.append("roles", {"role": CUSTOMER_ROLE})
        doc.save(ignore_permissions=True)

    if not frappe.db.exists("Contact", {"email_id": doc.email}):
        contact = frappe.new_doc("Contact")
        contact.first_name = doc.first_name or doc.email.split("@")[0]
        contact.last_name = doc.last_name or ""
        contact.append("email_ids", {"email_id": doc.email, "is_primary": 1})
        contact.user = doc.name
        contact.insert(ignore_permissions=True)
