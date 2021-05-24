import enum

from annotations import Annotations


class Richtext:
    def __init__(self, plain_text, href, annotations, type):
        self.plain_text = plain_text
        self.href = href
        self.annotations = Annotations
        self.type = Type


class Type(enum.Enum):
    text = 1
    mention = 2
    equation = 3
