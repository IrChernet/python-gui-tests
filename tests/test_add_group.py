def test_add_group(app):
    name_gr = "my new group"
    old_group_list = app.groups.get_group_list()
    app.groups.add_new_group(name_gr)
    new_group_list = app.groups.get_group_list()
    old_group_list.append(name_gr)
    assert sorted(old_group_list) == sorted(new_group_list)
