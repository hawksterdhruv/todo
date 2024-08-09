from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .handlers import (get_all_todos_handler, add_todo_handler)
from .schemas import Todo

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


# router = APIRouter()

# app.include_router(router)

@app.get('/')
async def get_home():
    return {'message': 'hello world'}


@app.get('/api/todos')
async def get_all_todos() -> list[Todo]:
    todos = get_all_todos_handler()
    return todos


@app.post('/api/todo')
async def add_todo(todo: Todo) -> Todo:
    todo = add_todo_handler(todo)
    return todo


if __name__ == '__main__':
    pass
