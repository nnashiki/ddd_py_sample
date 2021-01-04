from ec.infra.interface.user import IUserRepository
from injector import inject
from ec.domain.service.user import UserService
from ec.domain.model.user import User
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
