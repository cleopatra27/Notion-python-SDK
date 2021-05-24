import enum


class Number:
    def __init__(self, format):
        self.format = Format

class Format(enum.Enum):
    number = 1
    number_with_commas = 2
    percent = 3
    dollar = 4
    euro = 5
    pound = 6
    yen = 7
    ruble = 8
    rupee = 9
    won = 10
    yuan = 11

