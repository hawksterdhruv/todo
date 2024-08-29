import logging

from sqlalchemy.orm import Session

from . import models
from . import schemas

logger = logging.getLogger('uvicorn.handler')
logger.setLevel(logging.INFO)


def get_all_todos_handler(db: Session):
    return db.query(models.Todo).all()


def add_todo_handler(db: Session, todo: schemas.TodoCreate) -> models.Todo:
    db_todo = models.Todo(**todo.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def get_todo_handler(db: Session, todo_id: int) -> models.Todo:
    return db.query(models.Todo).filter(models.Todo.id == todo_id).one()  # type:ignore


def update_todo_handler(db: Session, todo_id, todo_raw) -> models.Todo:
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).update(todo_raw)  # type:ignore
    db.commit()
    return todo
