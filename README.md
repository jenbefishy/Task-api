# Task-API

This application, based on FastAPI, provides a RESTful API for task management. Users can view, add, delete, and sort tasks, which are stored in a PostgreSQL database.

## Libraries Used
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/latest/)
- [Uvicorn](https://www.uvicorn.org/)

## Installation

The application is built using [Docker](https://www.docker.com/).
```bash
git clone https://github.com/jenbefishy/Task-api/

docker-compose build

docker-compose run
```
## Routes
All routes are asynchronous, which allows for efficient handling of I/O operations. Here is a brief description of each route:

- **POST /tasks**: 
  - **Purpose**: Add a new task.
- **GET /tasks**: 
  - **Purpose**: Retrieve a list of all tasks.
- **GET /tasks/finished/**: 
  - **Purpose**: Retrieve a list of all completed tasks.
- **GET /tasks/unfinished/**: 
  - **Purpose**: Retrieve a list of all incomplete tasks.
- **DELETE /tasks/finished/**: 
  - **Purpose**: Delete all completed tasks.
