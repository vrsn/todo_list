from unittest import TestCase

from todo_app.constants import TODO_LIST_HARDCODED_NAME
from todo_app.models import ToDoItem
from todo_app.utils import todo_list_from_dict


class TestTodoListFromDict(TestCase):
    def test_trivial_case(self):
        test_dict = {
            "key1": "val1",
            "key2": "val2"
        }
        expected_list = [
            ToDoItem(item_id="key1", description="val1"),
            ToDoItem(item_id="key2", description="val2")
        ]

        res = todo_list_from_dict(test_dict)

        assert res.name == TODO_LIST_HARDCODED_NAME
        assert res.items_list == expected_list

    def test_empty_dict(self):
        res = todo_list_from_dict({})

        assert res.name == TODO_LIST_HARDCODED_NAME
        assert res.items_list == []
