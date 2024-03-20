from passlib.context import CryptContext
from datetime import timedelta
from config import settings

# Создаем объект для хеширования паролей
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Настройки для создания JWT токенов
ACCESS_TOKEN_EXPIRE_MINUTES = 30
SECRET_KEY = settings.SECRET_KEY  # Секретный ключ для подписи токенов

# Настройки для создания refresh-токенов
REFRESH_TOKEN_EXPIRE_DAYS = 30

ALGORITHM = settings.ALGORITHM
