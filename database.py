import os
from typing import Optional
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@db/postgres')

# Create async engine and session
engine = create_async_engine(DATABASE_URL)
new_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Declarative base model
Base = declarative_base()


class TaskOrm(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]
    isfinished: Mapped[bool]


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
