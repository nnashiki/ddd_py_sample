from fastapi import APIRouter, Depends
from pydantic import BaseModel

from ec.app.user import UserAppService, gen_app_with_di

router = APIRouter()


class User(BaseModel):
    name: str


@router.post("/v1/user")
def create_user(user: User, user_app_service: UserAppService = Depends(gen_app_with_di)):
    created_user = user_app_service.register(user.name)

    return {"user": created_user.name}
