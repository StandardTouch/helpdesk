import frappe
from frappe.query_builder import DocType, Query


def query_get_one(q: Query) -> dict:
    r = q.run(as_dict=True)

    if len(r) != 1:
        return

    return r.pop()


def default_outgoing_email_account():
    QBEmailAccount = DocType("Email Account")

    r = (
        frappe.qb.from_(QBEmailAccount)
        .select(QBEmailAccount.star)
        .where(QBEmailAccount.default_outgoing == 1)
        .limit(1)
    )

    return query_get_one(r)


def get_helpdesk_email_account():
    """
    Returns the configured Email Account for Helpdesk communication:
    1. HD Email Settings (Single DocType)
    2. HD Settings (Single DocType)
    """
    try:
        email_account_name = frappe.db.get_single_value(
            "HD Email Settings", "email_account"
        )
        if email_account_name and frappe.db.exists("Email Account", email_account_name):
            account = frappe.get_doc("Email Account", email_account_name)
            if account.enable_outgoing:
                return account
    except Exception:
        pass

    try:
        support_email = frappe.db.get_single_value(
            "HD Settings", "support_email_account"
        )
        if support_email and frappe.db.exists("Email Account", support_email):
            account = frappe.get_doc("Email Account", support_email)
            if account.enable_outgoing:
                return account
    except Exception:
        pass

    return None


def default_ticket_outgoing_email_account():
    # Priority 1: Helpdesk Email Settings or HD Settings
    if account := get_helpdesk_email_account():
        return account

    QBEmailAccount = DocType("Email Account")
    QBImapFolder = DocType("IMAP Folder")

    # Priority 2: Account with folder append_to = "HD Ticket"
    r = (
        frappe.qb.from_(QBEmailAccount)
        .select(QBEmailAccount.star)
        .inner_join(QBImapFolder)
        .on(QBImapFolder.parent == QBEmailAccount.name)
        .where(QBImapFolder.append_to == "HD Ticket")
        .where(QBEmailAccount.enable_outgoing == 1)
        .limit(1)
    )

    return query_get_one(r)

