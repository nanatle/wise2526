import math
from UE9_1 import Figur

class Punkt:
    def __init__(self, x: float = 0, y: float = 0):
        self._x = x
        self._y = y

    def distance(self, punkt):
        dx = punkt._x - self._x
        dy = punkt._y - self._y
        return (dx**2 + dy**2)**0.5

    def shift(self, x_val, y_val):
        self._x += x_val
        self._y += y_val

    def show(self):
        return f"Punkt({self._x}, {self._y})"


class Circle(Figur):
    def __init__(self, x: float = 0, y: float = 0, radius: float = 1):
        super().__init__()
        self._x = x
        self._y = y
        self._radius = radius

    def contains(self, p):
        abstand = math.sqrt((p._x - self._x)**2 + (p._y - self._y)**2)
        return abstand <= self._radius

    def intersect(self, c):
        abstand = math.sqrt((c._x - self._x)**2 + (c._y - self._y)**2)
        return abstand <= (self._radius + c._radius)

    def distance(self, obj):
        dx = obj._x - self._x
        dy = obj._y - self._y
        abim = math.sqrt(dx*dx + dy*dy)

        if type(obj) == Punkt:
            if abim <= self._radius:
                return 0
            return abs(abim - self._radius)

        if type(obj) == Circle:
            if abim <= self._radius + obj._radius:
                return 0
            return abs(abim - (self._radius + obj._radius))

    def shift(self, x_val, y_val):
        self._x += x_val
        self._y += y_val

    def scale(self, factor):
        self._radius *= factor

    def show(self):
        return f"Kreis: Mittelpunkt({self._x}, {self._y}), Radius: {self._radius}"
