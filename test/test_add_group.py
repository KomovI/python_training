# -*- coding: utf-8 -*-
import pytest
from model.group import Group


def test_add_group(app, db, check_ui, json_groups):
    old_groups = db.get_group_list()
    test_group = json_groups
    app.group.create(test_group)
    new_groups = db.get_group_list()
    old_groups.append(test_group)
    print(old_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)