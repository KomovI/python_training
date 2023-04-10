# -*- coding: utf-8 -*-
import random
import string
import pytest
from model.contact import Contact


def test_add_contact(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contact_list()
    # In tests for modification of contacts for variable anniversaryMonth, set the month with a small first letter.
    # In tests for adding contacts for variable anniversaryMonth, set the month with a capital first letter.
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
