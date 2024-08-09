import logging

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .handlers import (get_all_todos_handler, add_todo_handler)
from .schemas import Todo

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# router = APIRouter()

# app.include_router(router)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@app.get("/")
async def read_item(request: Request) -> HTMLResponse:
    todos = get_all_todos_handler()
    logger.info(todos)
    return templates.TemplateResponse(request=request, name="todos.html",
                                      context={'todos': todos})


@app.get('/api/todos')
async def get_all_todos() -> list[Todo]:
    todos = get_all_todos_handler()
    return todos


@app.post('/api/todo')
async def add_todo(todo: Todo) -> Todo:
    todo = add_todo_handler(todo)
    return todo


if __name__ == '__main__':
    # uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
    pass
