# Todo

## Run in development environment
```shell
./tailwindcss -i static/input.css -o static/output.css --watch
```
```shell
uvicorn src.main:app --reload --log-level info --port 5001
```
or
```shell
fastapi dev src --port 8001
```

## Upcoming features
- [x] Display Dashboard
- [x] add new tasks
- [x] add htmx
- [x] update status for tasks
- [x] icon for status
  - https://fontawesome.com/search?q=checkbox&o=r&m=free
- [x] Onclick open detail view for a task
- [x] comments for tasks
- [x] switch to sqlite
  - [x] auto increment for tasks / uuid?
- [x] Move done to a new tab
- [x] Tags for tasks
  - Filter for tags
- End date for tasks
- Allow edit for tasks
  - On double click ? Same as details pane ? 
- Allow to delete tasks or add a "not to be done" status
  - Hide these tasks
- Search for tasks
- Allow multiline comment. Currently triggers save on `Enter`
- Format comments and comments_input
- Change label colors