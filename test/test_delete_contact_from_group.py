from model.group import Group
from model.contact import Contact
import random


def test_delete_contact_from_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if app.contact.count() == 0:
        app.contact.create(Contact())
    test_group = random.choice(orm.get_group_list())
    test_contact = random.choice(orm.get_contact_list())
    if test_contact not in orm.get_contacts_in_group(test_group):
        print("\n Контакта \n %s \n нет в группе \n %s \n сначала добавим контакт в группу" %
              (test_contact, test_group))
        app.contact.add_contact_to_group(contact_id=test_contact.id, group_id=test_group.id)
        assert test_contact in orm.get_contacts_in_group(test_group)
    print("\n Удаляем контакт \n %s \n из группы \n %s" % (test_contact, test_group))
    app.contact.delete_contact_from_group(contact_id=test_contact.id, group_id=test_group.id)
    assert test_contact in orm.get_contacts_not_in_group(test_group)

