import logging

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from jinja2_fragments.fastapi import Jinja2Blocks

from .db import get_max_index
from .handlers import (get_all_todos_handler, add_todo_handler)
from .schemas import Todo

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Blocks(directory="templates")

# router = APIRouter()

# app.include_router(router)

logger = logging.getLogger('uvicorn')
logger.setLevel(logging.INFO)

max_index = get_max_index()


@app.get("/")
async def read_item(request: Request):
    todos = get_all_todos_handler()
    return templates.TemplateResponse(name="todos.html",
                                      context={'todos': todos, 'request': request})


@app.post('/')
async def add_todo(request: Request):
    raw_todo = await request.json()
    todo = Todo(**raw_todo)
    global max_index
    todo.id = max_index + 1
    logger.info(todo)
    todo = add_todo_handler(todo)
    max_index += 1
    return templates.TemplateResponse(name="todos.html",
                                      context={'todo': todo, 'request': request},
                                      block_name='task')


if __name__ == '__main__':
    pass
