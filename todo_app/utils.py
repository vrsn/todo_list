from todo_app.models import ToDoList, ToDoItem


def todo_list_from_dict(dict_instance: dict) -> ToDoList:
    todo_items = []
    for _k, _v in dict_instance.items():
        todo_items.append(ToDoItem(item_id=_k, description=_v))

    return ToDoList(items_list=todo_items)
