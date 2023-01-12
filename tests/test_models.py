from unittest import TestCase

from pydantic import ValidationError

from todo_app.constants import TODO_LIST_HARDCODED_NAME
from todo_app.models import ToDoItem, ToDoList


class TestToDoItem(TestCase):
    def test_trivial_case(self):
        ToDoItem(item_id="test_id", description="test_description")

    def test_mandatory_fields(self):
        with self.assertRaises(ValidationError):
            ToDoItem(description="test_description")
            ToDoItem(item_id="test_id")


class TestToDoList(TestCase):
    def test_default_name_with_items(self):
        todo_item1 = ToDoItem(item_id="test_id", description="test_description")
        todo_item2 = ToDoItem(item_id="test_id", description="test_description")
        todo_list = ToDoList(items_list=[todo_item1, todo_item2])

        assert todo_list.name == TODO_LIST_HARDCODED_NAME
        assert len(todo_list.items_list) == 2

    def test_custom_name_list_without_items(self):
        list_name = "Test Name"
        todo_list = ToDoList(name=list_name)

        assert todo_list.name == list_name
