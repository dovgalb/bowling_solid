from solid.ocp.wrong_shape_app.shape import ShapeType


class Circle:
    def __init__(self, its_type: ShapeType, its_radius: float, its_renter) -> None:
        self.itsType = its_type
        self.itsRadius = its_radius
        self.itsCenter = its_renter


def draw_circle(circle: Circle) -> None:
    pass