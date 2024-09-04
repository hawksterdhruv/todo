from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class StatusEnum(str, Enum):
    # todo: make statuses configurable
    done = 'done'
    in_progress = 'in progress'
    removed = 'removed'
    blocked = 'blocked'


class TodoBase(BaseModel):
    task: str
    created_at: datetime = datetime.now()
    status: StatusEnum = StatusEnum.in_progress


class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):
    id: int | None

    class Config:
        orm_model = True
    # child tasks
    # tags


class Comment(BaseModel):
    id: int
    comment: str

    class Config:
        orm_model = True


class TagBase(BaseModel):
    tag: str


class TagCreate(TagBase):
    pass


class Tag(TagBase):
    id: int | None

    class Config:
        orm_model = True
