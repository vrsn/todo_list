from fastapi import FastAPI, Path, status

from todo_app.models import ToDoItem, ToDoList
from todo_app.redis import get_redis_client

app = FastAPI(title="simple ToDo list")


redis_client = get_redis_client()


@app.get("/")
def root():
    return "Working. Go to /docs for API descriptions"


@app.post(
    "/todo_list",
    status_code=status.HTTP_201_CREATED,
    summary="Create a todo item",
)
def create_todo_item(todo_item: ToDoItem):
    return redis_client.add_or_replace_todo_item(todo_item)


@app.get(
    "/todo_list",
    status_code=status.HTTP_200_OK,
    summary="Get full todo list",
    response_model=ToDoList,
)
def get_todo_list():
    return redis_client.get_todo_list()


@app.put(
    "/todo_list/{item_id}",
    status_code=status.HTTP_200_OK,
    summary="Replace a todo item using item_id",
)
def replace_todo_item(
        new_description: str,
        item_id: str = Path(..., title="The id of the item to replace"),
):
    todo_item = ToDoItem(item_id=item_id, description=new_description)
    return redis_client.add_or_replace_todo_item(todo_item)


@app.get(
    "/todo_list/{item_id}",
    status_code=status.HTTP_200_OK,
    summary="Get a todo item by item_id",
    response_model=ToDoItem,
)
def get_todo_item(item_id: str = Path(..., title="The id of the item to get")):
    return redis_client.get_a_todo_item_by_id(item_id)


@app.delete(
    "/todo_list/{item_id}",
    status_code=status.HTTP_200_OK,
    summary="Delete a todo item by item_id",
)
def delete_todo_item(item_id: str = Path(..., title="The id of the item to delete")):
    redis_client.delete_todo_item(item_id)


@app.delete(
    "/todo_list",
    status_code=status.HTTP_200_OK,
    summary="Delete the whole todo list",
)
def delete_todo_list():
    return redis_client.delete_todo_list()
