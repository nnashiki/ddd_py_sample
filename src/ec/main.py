from injector import Injector, inject, Module, singleton, provider
from ec.domain.service.user import UserService
from ec.infra.interface.user import IUserRepository
from ec.infra.memory.user import UserInMemoryRepository


def configure_for_testing(binder):
    # Configurationクラスとして、中身は“configuration”を束縛
    binder.bind(IUserRepository, to=UserInMemoryRepository(), scope=singleton)


class DatabaseModule(Module):

    @provider
    @singleton
    def provide_repo(self, repo: UserInMemoryRepository) -> UserInMemoryRepository:
        return repo


if __name__ == "__main__":
    injector = Injector([configure_for_testing, DatabaseModule()])
    user_service = injector.get(UserService)
    created_user = user_service.create_user('foo')
    print(created_user.identity)
    stored_user = user_service.find_by_identity(created_user.identity)

    # assert created_user == stored_user
