from fastapi import APIRouter
from pydantic import BaseModel

from injector import Injector, inject, Module, singleton, provider
from ec.app.user import UserAppService
from ec.infra.interface.user import IUserRepository
from ec.infra.memory.user import UserInMemoryRepository

router = APIRouter()


class User(BaseModel):
    name: str


@router.post("/v1/user")
def create_user(user: User):
    user_app_service = startup()

    created_user = user_app_service.register(user.name)

    return {"user": created_user.name}


def startup() -> UserAppService:
    """依存解決を実行"""
    injector = Injector([configure_for_testing, DatabaseModule()])
    return injector.get(UserAppService)


def configure_for_testing(binder):
    # Configurationクラスとして、中身は“configuration”を束縛
    binder.bind(IUserRepository, to=UserInMemoryRepository(), scope=singleton)


class DatabaseModule(Module):

    @provider
    @singleton
    def provide_repo(self, repo: IUserRepository) -> UserInMemoryRepository:
        return repo
