from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship

from .db import Base

todo_tag = Table(
    'todo_tag', Base.metadata,
    Column(Integer, ForeignKey('todo.id')),
    Column(Integer, ForeignKey('tag.id'))
)


class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    task = Column(String)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    comments = relationship('Comment', back_populates='todo')
    tags = relationship('Tag', secondary=todo_tag, back_populates='todos')
    # is_active = Column(Boolean, default=True)


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    comment = Column(String)
    todo_id = Column(Integer, ForeignKey('todo.id'))
    created_at = Column(DateTime, default=datetime.now())
    todos = relationship('Todo', back_populates='comments')


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tag = Column(String)
    todos = relationship('Todo', secondary=todo_tag, back_populates='tags')
