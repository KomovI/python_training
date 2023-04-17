import re


def test_contact_on_home_page(app, db):
    contacts_from_db = db.get_contact_list()
    for contact_from_home_page in app.contact.get_contact_list():
        contact_from_db = contacts_from_db[contacts_from_db.index(contact_from_home_page)]
        assert contact_from_home_page.firstname == contact_from_db.firstname.strip()
        assert contact_from_home_page.lastname == contact_from_db.lastname.strip()
        assert contact_from_home_page.address == contact_from_db.address.strip()
        assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_db)
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)
        print(merge_phones_like_on_home_page(contact_from_db))


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), [contact.homePhone, contact.mobilePhone,
                                                                        contact.workPhone,
                                                                        contact.secondaryHomePhone])))


def delete_extra_spaces(s):
    return re.sub(" +", " ", s)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: delete_extra_spaces(x), [contact.email1.strip(), contact.email2.strip(),
                                                                        contact.email3.strip()])))
