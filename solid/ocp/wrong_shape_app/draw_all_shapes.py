from solid.ocp.wrong_shape_app.circle import draw_circle
from solid.ocp.wrong_shape_app.shape import Shape, ShapeType
from solid.ocp.wrong_shape_app.square import draw_square


def draw_all_shapes(list: list[Shape]) -> None:
    """
    Функция для отрисовки всех фигур из списка.

    Args:
    list (list[Shape]): Список фигур.
    """
    for s in list:
        if s.its_type == ShapeType.square:
            draw_square(s)
        elif s.its_type == ShapeType.circle:
            draw_circle(s)