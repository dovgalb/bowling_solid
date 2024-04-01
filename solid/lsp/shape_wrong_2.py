class Rectangle:
    def __init__(self) -> None:
        self.top_left: Point
        self.width: float
        self.height: float

    @property
    def width(self) -> float:
        return self.width

    @width.setter
    def width(self, value: float) -> None:
        self.width = value

    @property
    def height(self) -> float:
        return self.height

    @height.setter
    def height(self, value: float) -> None:
        self.height = value