from model.contact import Contact
from random import randrange


def test_delete_some_contact(app):
    # In method for modification of contacts for variable anniversaryMonth, set the month with a small first letter.
    # In method for adding contacts for variable anniversaryMonth, set the month with a capital first letter.
    if app.contact.count() == 0:
        app.contact.create(Contact())
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

