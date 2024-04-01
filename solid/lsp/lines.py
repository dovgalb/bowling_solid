class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class LinearObject:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    @property
    def P1(self):
        return self.p1

    @property
    def P2(self):
        return self.p2

    @property
    def Slope(self):
        # код для вычисления наклона
        pass

    @property
    def YIntercept(self):
        # код для вычисления пересечения с осью Y
        pass

    def IsOn(self, p):
        # код проверки принадлежности точки
        pass

class Line(LinearObject):
    def __init__(self, p1, p2):
        super().__init__(p1, p2)

    def IsOn(self, p):
        # код для Line проверки принадлежности точки
        pass

class LineSegment(LinearObject):
    def __init__(self, p1, p2):
        super().__init__(p1, p2)

    def GetLength(self):
        # код для вычисления длины отрезка
        pass

    def IsOn(self, p):
        # код для LineSegment проверки принадлежности точки
        pass