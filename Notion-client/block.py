import enum


class Block:
    def __init__(self, id, created_time, last_edited_time, has_children, object):
        self.id = id
        self.created_time = created_time
        self.last_edited_time = last_edited_time
        self.last_edited_time = last_edited_time
        self.has_children = has_children
        self.object = "block"


class Type(enum.Enum):
    paragraph = 1
    heading_1 = 2
    heading_2 = 3
    heading_3 = 4
    bulleted_list_item = 5
    numbered_list_item = 6
    to_do = 7
    toggle = 8
    child_page = 9
    unsupported = 10
