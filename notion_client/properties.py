import enum


class Properties:
    def __init__(self, name, type):
        self.name = name
        self.type = Type


class Type(enum.Enum):
    title = 1
    rich_text = 2
    number = 3
    date = 4
    select = 5
    multi_select = 6
    people =7
    file = 8
    checkbox = 9
    url = 10
    email = 11
    phone_number = 12
    formula = 13
    relation = 14
    rollup = 15
    created_time = 15
    created_by = 16
    last_edited_time = 17
    last_edited_by = 18
