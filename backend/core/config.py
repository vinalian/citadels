from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    # Настройки для подключения к базе данных PostgreSQL
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    # Настройки для подключения к Redis
    REDIS_HOST: str
    REDIS_PORT: int

    # Секретный ключ для JWT
    SECRET_KEY: str

    # Алгоритм хеширования JWT
    ALGORITHM: str

    class Config:
        env_file = ".env"


settings = Settings()
