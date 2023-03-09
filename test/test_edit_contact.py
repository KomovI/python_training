# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    # In tests for modification of contacts for variable anniversaryMonth, set the month with a small first letter.
    # In tests for adding contacts for variable anniversaryMonth, set the month with a capital first letter.
    app.contact.edit_first_contact(Contact(firstname="TestEdit", middlename="TesterovichEdit", lastname="TesterovEdit",
                                           nickname="QA EDIT", title="QA manager EDIT", company="Test Company EDIT",
                                           address="Test Address EDIT", home="Test Home Telephone EDIT",
                                           mobile="Test Mobile Telephone EDIT", work="Test Work Telephone EDIT",
                                           fax="Test Fax EDIT", email1="Test E-mail EDIT", email2="Test E-mail2 EDIT",
                                           email3="Test E-mail3 EDIT", homepage="Test Homepage EDIT",
                                           birthdayDay="5", birthdayMonth="April", birthdayYear="2007",
                                           anniversaryDay="8", anniversaryMonth="november", anniversaryYear="2009",
                                           secondaryAddress="Test Secondary Address EDIT",
                                           secondaryHome="Test Home EDIT", notes="Test Notes EDIT"))
    app.session.logout()
