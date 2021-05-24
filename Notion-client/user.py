import enum


class User:
    def __init__(self, object, id, type, name, avatar_url):
        self.object = "user"
        self.id = id
        self.type = Type
        self.name = name
        self.avatar_url = avatar_url


class Type(enum.Enum):
    person = 1
    bot = 2