class Rectangle:
    def __init__(self, topLeft: Point, width: float, height: float):
        self.topLeft = topLeft
        self.width = width
        self.height = height

    @property
    def Width(self) -> float:
        return self.width

    @Width.setter
    def Width(self, value: float) -> None:
        self.width = value

    @property
    def Height(self) -> float:
        return self.height

    @Height.setter
    def Height(self, value: float) -> None:
        self.height = value