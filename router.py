from typing import Annotated, List

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)


@router.post("", response_model=STaskId)
async def add_task(task: Annotated[STaskAdd, Depends()]) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return STaskId(ok=True, task_id=task_id)


@router.get("", response_model=List[STask])
async def get_tasks() -> List[STask]:
    tasks = await TaskRepository.find_all()
    return tasks


@router.get("/finished/", response_model=List[STask])
async def get_finished_tasks() -> List[STask]:
    tasks = await TaskRepository.find_all_finished()
    return tasks


@router.get("/unfinished/", response_model=List[STask])
async def get_unfinished_tasks() -> List[STask]:
    tasks = await TaskRepository.find_all_unfinished()
    return tasks


@router.delete("/finished/", response_model=dict)
async def delete_finished_tasks():
    tasks_count = await TaskRepository.delete_all_finished()
    return {"ok": True, "count": tasks_count}

