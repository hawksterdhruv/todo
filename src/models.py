from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .db import Base


class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    task = Column(String)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    comments = relationship('Comment', back_populates='todo')
    # is_active = Column(Boolean, default=True)

    # items = relationship("Item", back_populates="owner")


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    comment = Column(String)
    todo_id = Column(Integer, ForeignKey('todo.id'))
    created_at = Column(DateTime, default=datetime.now())
    todo = relationship('Todo', back_populates='comments')
    # f_key to todos
