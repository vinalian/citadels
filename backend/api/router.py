from fastapi import APIRouter

user_router = APIRouter()


@user_router.get('/user')
async def register_user():
    return {"status": "ok"}
