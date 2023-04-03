# -*- coding: utf-8 -*-
import random
import string
import pytest
from model.contact import Contact


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
         "December", "-"]


def random_day():
    day = random.choice([""] + list([str(i) for i in range(32)]))
    return day


testdata = [Contact(firstname="", middlename="", lastname="", nickname="",
                    title="", company="", address="", home="",
                    mobile="", work="", fax="", email1="",
                    email2="", email3="", homepage="", birthdayDay="",
                    birthdayMonth="-", birthdayYear="", anniversaryDay="", anniversaryMonth="-",
                    anniversaryYear="", secondaryAddress="", secondaryHome="",
                    notes="")] + [
               Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 20),
                       lastname=random_string("lastname", 20), nickname=random_string("nickname", 20),
                       title=random_string("title", 20), company=random_string("company", 20),
                       address=random_string("address", 20), home=random_string("home", 20),
                       mobile=random_string("mobile", 20), work=random_string("work", 20),
                       fax=random_string("fax", 20), email1=random_string("footer", 20),
                       email2=random_string("email2", 20), email3=random_string("email3", 20),
                       homepage=random_string("homepage", 20), birthdayDay=random_day(),
                       birthdayMonth=random.choice(month), birthdayYear=random_string("", 4),
                       anniversaryDay=random_day(), anniversaryMonth=random.choice(month),
                       anniversaryYear=random_string("", 4), secondaryAddress=random_string("secondaryAddress", 20),
                       secondaryHome=random_string("secondaryHome", 20), notes=random_string("notes", 20))
               for i in range(5)
           ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    # In tests for modification of contacts for variable anniversaryMonth, set the month with a small first letter.
    # In tests for adding contacts for variable anniversaryMonth, set the month with a capital first letter.
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
