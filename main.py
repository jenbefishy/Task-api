from fastapi import FastAPI
from database import delete_tables, create_tables
from router import router as tasks_router


async def startup():
    await delete_tables()
    print("Deleted tables")
    await create_tables()
    print("Created tables")

app = FastAPI(on_startup=[startup])

app.include_router(tasks_router)

