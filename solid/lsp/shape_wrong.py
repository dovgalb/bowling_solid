from enum import Enum


class ShapeType(Enum):
    square = 1
    circle = 2


class Shape:
    def __init__(self, t: ShapeType) -> None:
        self.type = t

    @staticmethod
    def draw_shape(s: 'Shape') -> None:
        if s.type == ShapeType.square:
            s.draw()
        elif s.type == ShapeType.circle:
            s.draw()


class Circle(Shape):
    def __init__(self) -> None:
        super().__init__(ShapeType.circle)
        self.center: Point
        self.radius: float

    def draw(self) -> None:
        pass  # рисует круг


class Square(Shape):
    def __init__(self) -> None:
        super().__init__(ShapeType.square)
        self.top_left: Point
        self.side: float

    def draw(self) -> None:
        pass  # рисует квадрат


class Point:
    def __init__(self) -> None:
        self.x: float
        self.y: float


