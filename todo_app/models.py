from typing import Optional

from pydantic import BaseModel

from todo_app.constants import TODO_LIST_HARDCODED_NAME


class ToDoItem(BaseModel):
    item_id: str
    description: str


class ToDoList(BaseModel):
    name: str = TODO_LIST_HARDCODED_NAME
    items_list: Optional[list[ToDoItem]]
