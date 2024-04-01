from enum import Enum


class ShapeType(Enum):
    circle = 1
    square = 2


class Shape:
    def __init__(self, its_type: ShapeType) -> None:
        self.its_type = its_type
