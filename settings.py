from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import os

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")

DATABASE_URL = (
    f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@"
    + f"{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Создание асинхронного движка SQLAlchemy
async_engine = create_async_engine(DATABASE_URL, echo=True)

# Создание фабрики сессий SQLAlchemy
async_session = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)

