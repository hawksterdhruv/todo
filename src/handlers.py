import logging

from sqlalchemy.orm import Session

from . import models
from . import schemas

logger = logging.getLogger('uvicorn')
logger.setLevel(logging.INFO)


def get_completed_todos_handler(db: Session):
    logger.info(db.query(models.Todo).filter_by(status='done'))
    return db.query(models.Todo).filter_by(status='done')


def get_incomplete_todos_handler(db: Session):
    logger.info(db.query(models.Todo).filter_by(status='in progress'))
    return db.query(models.Todo).filter_by(status='in progress')


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


def update_todo_tag_handler(db: Session, todo_id, todo_raw) -> models.Todo:
    tag = db.query(models.Tag).filter(models.Tag.id == todo_raw['tag_id']).one()  # type:ignore
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).one()  # type:ignore
    todo.tags.append(tag)
    db.commit()
    return todo


def get_all_tags_handler(db: Session) -> list[type[models.Tag]]:
    return db.query(models.Tag).all()


def add_tag_handler(db: Session, tag_raw: schemas.TagCreate) -> models.Tag:
    db_tag = models.Tag(**tag_raw.model_dump())
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag


def add_comment_handler(todo_id, raw_comment, db: Session) -> models.Comment:
    todo: models.Todo = db.query(models.Todo).filter(models.Todo.id == todo_id).one()  # type:ignore
    db_comment = models.Comment(**raw_comment.model_dump())
    todo.comments.append(db_comment)
    db.add(db_comment)
    db.add(todo)
    db.commit()
    db.refresh(db_comment)
    return db_comment
