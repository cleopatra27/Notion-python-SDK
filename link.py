import enum


class Link:
    def __init__(self, url, type):
        self.url = url
        self.type = Type


class Type(enum.Enum):
    user - 1
    page = 2
    database = 3
    date= 4