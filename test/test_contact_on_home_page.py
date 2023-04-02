import re
from random import randrange


def test_contact_on_home_page(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_full_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    print(merge_phones_like_on_home_page(contact_from_edit_page))


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), [contact.homePhone, contact.mobilePhone,
                                                                        contact.workPhone,
                                                                        contact.secondaryHomePhone])))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", [contact.email1, contact.email2,
                                                                        contact.email3]))
