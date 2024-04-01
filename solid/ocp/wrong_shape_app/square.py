from solid.ocp.wrong_shape_app.shape import ShapeType


class Square:
    def __init__(self, its_type: ShapeType, its_side: float, its_top_left) -> None:
        self.its_type = its_type
        self.its_side = its_side
        self.its_top_left = its_top_left


def draw_square(square: Square) -> None:
    # Реализация функции DrawSquare
    pass