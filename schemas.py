from datetime import datetime

from pydantic import BaseModel

from enum import Enum


class StatusEnum(str, Enum):
    done = 'done'
    in_progress = 'in progress'


class Todo(BaseModel):
    id: int
    task: str
    created_at: datetime
    status: StatusEnum
    # child tasks
    # comments
    # tags


class Comment(BaseModel):
    pass


class Tag(BaseModel):
    pass
