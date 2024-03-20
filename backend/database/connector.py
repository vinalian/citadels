from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from backend.core.config import settings

# Создание асинхронного движка SQLAlchemy
DATABASE_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@" + \
               f"{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
async_engine = create_async_engine(DATABASE_URL, echo=True)

# Создание фабрики сессий SQLAlchemy
async_session = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)

# Базовый класс для моделей SQLAlchemy
Base = declarative_base()


class DatabaseSession:
    def __init__(self):
        self.Session = async_session

    def create_session(self):
        return self.Session()
