from abc import ABC, abstractmethod


class ShapeInterface(ABC):
    @abstractmethod
    def draw(self):
        raise NotImplemented


class Square(ShapeInterface):
    def draw(self):
        print('draw square')


class Circle(ShapeInterface):
    def draw(self):
        print('draw circle')


def DrawAllShapes(shapes: list[ShapeInterface]) -> None:
    """
    Функция для отрисовки всех фигур из списка.

    Args:
    shapes (List[Shape]): Список фигур.
    """
    for shape in shapes:
        shape.Draw()