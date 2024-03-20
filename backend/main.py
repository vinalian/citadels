from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.router import user_router

app = FastAPI()

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

    uvicorn.run(app, port=8001)
