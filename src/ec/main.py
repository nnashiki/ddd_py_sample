from injector import Injector, inject, Module, singleton, provider
from ec.domain.service.user import UserService
from ec.app.user import UserAppService
from ec.infra.interface.user import IUserRepository
from ec.infra.memory.user import UserInMemoryRepository


def configure_for_testing(binder):
    # Configurationクラスとして、中身は“configuration”を束縛
    binder.bind(IUserRepository, to=UserInMemoryRepository(), scope=singleton)


class DatabaseModule(Module):

    @provider
    @singleton
    def provide_repo(self, repo: IUserRepository) -> UserInMemoryRepository:
        return repo


def startup() -> UserAppService:
    """依存解決を実行"""
    injector = Injector([configure_for_testing, DatabaseModule()])
    return injector.get(UserAppService)


if __name__ == "__main__":
    user_app_service = startup()

    created_user = user_app_service.register('foo')
    print(created_user.identity)
    stored_user = user_app_service.show(created_user.identity)

    # assert created_user == stored_user
