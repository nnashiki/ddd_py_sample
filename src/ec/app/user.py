from ec.domain.service.user import UserService
from ec.domain.model.user import User
from injector import Injector, inject, Module, singleton, provider
from ec.infra.interface.user import IUserRepository
from ec.infra.memory.user import UserInMemoryRepository

import uuid


class UserAppService:
    """ アプリケーションとしての動き """

    @inject
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    def register(self, name):
        user_service = UserService(self.user_repo)
        user: User = user_service.create_user(name)
        return user

    def show(self, identity: uuid):
        user_service = UserService(self.user_repo)
        user: User = user_service.find_by_identity(identity)
        return user


def gen_app_with_di() -> UserAppService:
    """依存解決を実行"""

    def bind_repository(binder):
        binder.bind(IUserRepository, to=UserInMemoryRepository(), scope=singleton)

    class DatabaseModule(Module):

        @provider
        @singleton
        def provide_repo(self, repo: UserInMemoryRepository) -> UserInMemoryRepository:
            return repo

    injector = Injector([bind_repository, DatabaseModule()])
    return injector.get(UserAppService)


def gen_app_with_di_test() -> UserAppService:
    """依存解決を実行(テスト用)"""

    def bind_repository(binder):
        binder.bind(IUserRepository, to=UserInMemoryRepository(), scope=singleton)

    class DatabaseModule(Module):

        @provider
        @singleton
        def provide_repo(self, repo: IUserRepository) -> UserInMemoryRepository:
            return repo

    injector = Injector([bind_repository, DatabaseModule()])
    return injector.get(UserAppService)
