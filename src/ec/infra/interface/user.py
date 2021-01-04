from abc import ABCMeta, abstractmethod
from ec.domain.model.user import User
import uuid


class IUserRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find_by_identity(self, identity: uuid):
        pass

    @abstractmethod
    def store(self, user: User):
        pass
