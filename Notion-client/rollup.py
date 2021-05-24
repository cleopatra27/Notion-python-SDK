import enum


class Rollup:
    def __init__(self, relation_property_name, relation_property_id, rollup_property_name, rollup_property_id, function):
        self.relation_property_name = relation_property_name
        self.relation_property_id = relation_property_id
        self.rollup_property_name = rollup_property_name
        self.rollup_property_id = rollup_property_id
        self.function = Function


class Function(enum.Enum):
    count_all = 1
    count_values,= 2
    count_unique_values = 3
    count_empty = 4
    count_not_empty = 5
    percent_empty = 6
    percent_not_empty = 7
    sum = 8
    average = 9
    median = 10
    min = 11
    max = 12
    range= 13