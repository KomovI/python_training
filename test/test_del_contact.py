from model.contact import Contact


def test_delete_first_contact(app):
    # In method for modification of contacts for variable anniversaryMonth, set the month with a small first letter.
    # In method for adding contacts for variable anniversaryMonth, set the month with a capital first letter.
    if app.contact.count() == 0:
        app.contact.create(Contact())
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_firs_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts

