import logging

from .db import db
from .schemas import Todo
from tinydb import Query

logger = logging.getLogger('uvicorn.handler')
logger.setLevel(logging.INFO)


def get_all_todos_handler() -> list[Todo]:
    return [Todo(**a) for a in db.all()]


def add_todo_handler(todo: Todo) -> Todo:
    db.insert(dict(todo))
    return todo


def get_todo_handler(todo_id) -> Todo:
    todo_query = Query()
    todo_raw = db.search(todo_query.id == todo_id).pop()
    return Todo(**todo_raw)


def update_todo_handler(todo_id, todo_raw) -> Todo:
    logger.info(todo_id)
    logger.info(todo_raw)
    todo_query = Query()
    db.update(todo_raw, todo_query.id == todo_id)
    todo = get_todo_handler(todo_id)
    logger.info(todo)
    return todo
