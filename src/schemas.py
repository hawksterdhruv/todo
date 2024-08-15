from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class StatusEnum(str, Enum):
    # todo: make statuses configurable
    done = 'done'
    in_progress = 'in progress'
    removed = 'removed'
    blocked = 'blocked'


class Todo(BaseModel):
    id: int | None = None
    task: str
    created_at: datetime = datetime.now()
    status: StatusEnum = StatusEnum.in_progress
    # child tasks
    # comments
    # tags


class Comment(BaseModel):
    pass


class Tag(BaseModel):
    pass
