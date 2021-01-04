import uuid
from injector import inject
from ec.infra.interface.user import IUserRepository
from ec.infra.memory.user import UserInMemoryRepository
from ec.domain.model.user import User


class UserService:
    """ User Service on Application Layer"""

    @inject
    def __init__(self, repo: IUserRepository):
        self.repo = repo

    def create_user(self, name):
        user = User(uuid.uuid4(), name)
        self.repo.store(user)
        return user

    def find_by_identity(self, identity: uuid):
        return self.repo.find_by_identity(identity)
