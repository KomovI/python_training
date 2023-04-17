from model.contact import Contact
import random


def test_delete_some_contact(app, db, check_ui):
    # In method for modification of contacts for variable anniversaryMonth, set the month with a small first letter.
    # In method for adding contacts for variable anniversaryMonth, set the month with a capital first letter.
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact())
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    print(contact)
    app.contact.delete_contact_by_id(contact.id)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
