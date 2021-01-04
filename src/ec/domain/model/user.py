from typing import final
import uuid


class NameLengthException(Exception):
    pass


class User:
    def __init__(self, identity: uuid, name):
        self.identity: uuid = identity
        self.name = name
