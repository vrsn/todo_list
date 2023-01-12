from redis import Redis

from todo_app.constants import TODO_LIST_HARDCODED_NAME
from todo_app.models import ToDoItem, ToDoList
from todo_app.utils import todo_list_from_dict


class RedisClient:
    def __init__(self) -> None:
        self.cache = Redis(
            host="redis",
            port="6379",
            decode_responses=True,
        )

    # todo: remove
    def test_connection(self):
        self.cache.set('test', 'testing - fine')
        res = self.cache.get('test')
        self.cache.delete('test')
        return res

    def add_or_replace_todo_item(self, todo_item: ToDoItem, list_name: str = TODO_LIST_HARDCODED_NAME):
        return self.cache.hset(list_name, todo_item.item_id, todo_item.description)

    def get_a_todo_item_by_id(self, item_id: str, list_name: str = TODO_LIST_HARDCODED_NAME) -> ToDoItem:
        return ToDoItem(item_id=item_id, description=self.cache.hget(list_name, item_id))

    def get_todo_list(self, list_name: str = TODO_LIST_HARDCODED_NAME) -> ToDoList:
        return todo_list_from_dict(self.cache.hgetall(list_name))

    def delete_todo_item(self, item_id: str, list_name: str = TODO_LIST_HARDCODED_NAME):
        return self.cache.hdel(list_name, item_id)

    def delete_todo_list(self, list_name: str = TODO_LIST_HARDCODED_NAME):
        return self.cache.delete(list_name)


def get_redis_client() -> RedisClient:
    return RedisClient()
