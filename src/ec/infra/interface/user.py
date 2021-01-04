from abc import ABCMeta, abstractmethod
import uuid


class IUserRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def find_by_identity(self, identity: uuid):
        pass

    @abstractmethod
    def store(self):
        pass
