from helpdesk.patches.move_contact_dynamic_link_to_hd_customer import (
    migrate_contact_links_to_members,
)


def execute():
    """Portal signups were only linked to their customer through the Contact; add them as members."""
    migrate_contact_links_to_members()
