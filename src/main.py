import logging

from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from jinja2_fragments.fastapi import Jinja2Blocks
from sqlalchemy.orm import Session

from . import models
from .db import engine, SessionLocal
from .handlers import (get_incomplete_todos_handler, get_completed_todos_handler, add_todo_handler, update_todo_handler,
                       get_todo_handler, add_comment_handler)
from .schemas import TodoCreate

models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Blocks(directory="templates")

# router = APIRouter()

# app.include_router(router)

logger = logging.getLogger('uvicorn')
logger.setLevel(logging.INFO)


# max_index = get_max_index()


@app.get("/")
async def get_todos(request: Request, db: Session = Depends(get_db)):
    incomplete_todos = get_incomplete_todos_handler(db)
    completed_todos = get_completed_todos_handler(db)
    return templates.TemplateResponse(name="todos.html",
                                      context={'todos_incomplete': incomplete_todos, 'todos_done': completed_todos,
                                               'request': request})


@app.post('/')
async def add_todo(request: Request, db: Session = Depends(get_db)):
    raw_todo = await request.json()
    todo = TodoCreate(**raw_todo)
    todo = add_todo_handler(db, todo)

    return templates.TemplateResponse(name="todos.html",
                                      context={'todo_incomplete': todo, 'request': request},
                                      block_name='task_incomplete')


@app.get('/{todo_id}')
async def get_todo(todo_id: int, request: Request, db: Session = Depends(get_db)):
    todo = get_todo_handler(db, todo_id)
    return templates.TemplateResponse(name="todos.html",
                                      context={'todo_focus': todo, 'request': request},
                                      block_name='detail_view')


@app.put('/{todo_id}')
async def update_todo(todo_id: int, request: Request, db: Session = Depends(get_db)):
    raw_todo = await request.json()
    todo = update_todo_handler(db, todo_id, raw_todo)
    logger.info(todo)
    return templates.TemplateResponse(name="todos.html",
                                      context={'todo': todo, 'request': request},
                                      block_name='detail_view')


@app.post('/comment')
async def add_comment(request: Request, db: Session = Depends(get_db)):
    raw_comment = await request.json()
    comment = add_comment_handler(db, raw_comment)
    logger.info(comment)
    return templates.TemplateResponse(name='todo.html', context={'comment': comment, 'request': request},
                                      block_name='comment')


if __name__ == '__main__':
    pass
