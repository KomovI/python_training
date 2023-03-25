# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    # In tests for modification of contacts for variable anniversaryMonth, set the month with a small first letter.
    # In tests for adding contacts for variable anniversaryMonth, set the month with a capital first letter.
    contact = Contact(firstname="Test", middlename="Testerovich", lastname="Testerov", nickname="QA",
                      title="QA manager", company="Test Company", address="Test Address", home="Test Home Telephone",
                      mobile="Test Mobile Telephone", work="Test Work Telephone", fax="Test Fax", email1="Test E-mail",
                      email2="Test E-mail2", email3="Test E-mail3", homepage="Test Homepage", birthdayDay="1",
                      birthdayMonth="January", birthdayYear="2000", anniversaryDay="2", anniversaryMonth="January",
                      anniversaryYear="2005", secondaryAddress="Test Secondary Address", secondaryHome="Test Home",
                      notes="Test Notes")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
