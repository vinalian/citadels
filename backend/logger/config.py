from loguru import logger
import sys

# Настройки формата логов
logger.remove()
logger.add(sys.stderr, level="INFO", format="{time:DD-MM-YYYY at HH:mm:ss} | {level} | {message}")

# Настройки логирования в файл
logger.add("logs/logfile.log", rotation="500 MB", level="ERROR", encoding="utf-8", backtrace=True, diagnose=True)
