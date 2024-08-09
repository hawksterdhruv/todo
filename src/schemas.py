from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class StatusEnum(str, Enum):
    done = 'done'
    in_progress = 'in progress'


class Todo(BaseModel):
    id: int
    task: str
    created_at: datetime
    status: StatusEnum | None
    # child tasks
    # comments
    # tags


class Comment(BaseModel):
    pass


class Tag(BaseModel):
    pass
