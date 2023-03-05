# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Test", middlename="Testerovich", lastname="Testerov", nickname="QA",
                               title="QA manager", company="Test Company", address="Test Address",
                               home="Test Home Telephone", mobile="Test Mobile Telephone",
                               work="Test Work Telephone", fax="Test Fax", email1="Test E-mail",
                               email2="Test E-mail2", email3="Test E-mail3", homepage="Test Homepage",
                               birthdayDay="1", birthdayMonth="January", birthdayYear="2000",
                               anniversaryDay="2", anniversaryMonth="January", anniversaryYear="2005",
                               secondaryAddress="Test Secondary Address", secondaryHome="Test Home",
                               notes="Test Notes"))
    app.session.logout()
