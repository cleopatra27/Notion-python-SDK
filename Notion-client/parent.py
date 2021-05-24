import enum


class Parent:
    def __init__(self, databaseID, pageID, Parent):
        self.databaseID = databaseID
        self.pageID = pageID
        self.type = Type


class Type(enum.Enum):
    database_id = 1
    page_id = 2