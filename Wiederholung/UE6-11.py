#einfache geometrische Objekte
import math

class Point:

    def __init__(self, x: float, y: float):
        self._x: float = x
        self._y: float = y

    def distance(self, other: "Point") -> float:
        return math.sqrt((self._x - other._x) ** 2 + (self._y - other._y) ** 2)


    def shift(self, x_val: float, y_val: float):
        self._x = x_val + self._x
        self._y = y_val + self._y


    def show(self) :
        return f"Punkt: ({self._x}, {self._y})"



punkt = Point(1, 1)
punkt1 = punkt.shift(1, 1)
punkt.show()
punkt1.show()
punkt2 = Point (3, 4)
punkt2.show()
print(punkt.distance(punkt2))

