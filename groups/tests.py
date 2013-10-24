from django.test import TestCase
from groups.forms import CreateGroupForm
from groups.models import Group

class GroupsTest(TestCase):
    def test_valid_form(self):
        self.assertTrue(CreateGroupForm(data=dict(
            name="SDD 2014",
            key="key",
            visible=True
        )).is_valid())

    def test_visible_no_key(self):
        self.assertTrue(CreateGroupForm(data=dict(
            name="group1",
            key="",
            visible=True
        )).is_valid())

    def test_invisible_no_key(self):
        self.assertFalse(CreateGroupForm(data=dict(
            name="groupname",
            key="",
            visible=False
        )).is_valid())

    def test_repeat_name(self):
        Group.objects.create(
            name="used",
            key="",
            visible=False
        )
        self.assertFalse(CreateGroupForm(data=dict(
            name="used",
            key="",
            visible=False
        )).is_valid())
