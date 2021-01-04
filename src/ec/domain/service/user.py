import uuid
from injector import inject
from ec.infra.interface.user import IUserRepository
from ec.infra.memory.user import UserInMemoryRepository
from ec.domain.model.user import User


class UserService:
    """ ドメイン の中の不自然な処理を肩代わり"""

    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    def create_user(self, name) -> User:
        user = User(uuid.uuid4(), name)
        self.user_repo.store(user)
        return user

    def find_by_identity(self, identity: uuid) -> User:
        return self.user_repo.find_by_identity(identity)
