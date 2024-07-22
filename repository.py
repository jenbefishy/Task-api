from sqlalchemy import select, delete
from database import new_session, TaskOrm
from schemas import STaskAdd, STask


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.dict()
            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            return [STask.from_orm(task_model) for task_model in task_models]

    @classmethod
    async def find_all_finished(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskOrm).where(TaskOrm.isfinished == True)
            result = await session.execute(query)
            task_models = result.scalars().all()
            return [STask.from_orm(task_model) for task_model in task_models]

    @classmethod
    async def find_all_unfinished(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskOrm).where(TaskOrm.isfinished == False)
            result = await session.execute(query)
            task_models = result.scalars().all()
            return [STask.from_orm(task_model) for task_model in task_models]

    @classmethod
    async def delete_all_finished(cls) -> int:
        async with new_session() as session:
            query = delete(TaskOrm).where(TaskOrm.isfinished == True)
            result = await session.execute(query)
            await session.commit()
            return result.rowcount

