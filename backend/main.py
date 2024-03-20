from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.router import user_router
from logger.config import logger


app = FastAPI(logger=logger)

# Подключение CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение роутера
app.include_router(user_router, tags=['user'])


if __name__ == "__main__":
    import uvicorn

    logger.info("Start api")
    uvicorn.run(app, port=8001)
