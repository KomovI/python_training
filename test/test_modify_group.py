# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_modify_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group())
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    index = old_groups.index(group)
    new_group = Group(name="New group")
    new_group.id = group.id
    app.group.modify_group_by_id(new_group.id, new_group)
    new_groups = db.get_group_list()
    old_groups[index] = new_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
