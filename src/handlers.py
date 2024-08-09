from .db import db
from .schemas import Todo


def get_all_todos_handler() -> list[Todo]:
    return db.all()


def add_todo_handler(todo: Todo) -> Todo:
    db.insert(dict(todo))
    return todo
