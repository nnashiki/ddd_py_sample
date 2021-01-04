from ec.domain.model.user import User
from ec.domain.model.user import User
from ec.infra.interface.user import IUserRepository
import uuid


class UserInMemoryRepository(IUserRepository):

    def find_by_identity(self, identity: uuid):
        pass

    def store(self, user: User):
        print("store success")
