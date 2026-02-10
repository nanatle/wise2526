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
        return f"({self._x}, {self._y})"


class Circle:
    def __init__(self, p: Point, radius: float):
        self._radius: float = radius
        self._p: Point = p

    def distance(self, other: "Circle") -> float:
        return self._p.distance(other._p)

    def shift(self, x_val: float, y_val: float) -> None:
        self._p.shift(x_val, y_val)

    def show(self):
        return f"{self._p.show()}, Radius: {self._radius}"

    def scale(self, factor: float) -> None:
        self._radius *= factor

    def contains(self, other: "Circle") -> bool:
        return self.distance(other) + other._radius <= self._radius

    def intersects(self, other: "Circle") -> bool:
        d = self.distance(other)
        return abs(self._radius - other._radius) < d < (self._radius + other._radius)


p1 = Point(0, 0)
print("Punkt 1:", p1.show())

p1.shift(1, 1)
print("Verschoben P1:" , p1.show())

p2 = Point(2, 3)
print("Punkt 2:", p2.show())
print("Abstand zwischen P1 und P2:", p1.distance(p2))

k1 = Circle(Point(0, 0), 2.0)
print("Kreis1: ", k1.show())

k1.shift(1, 1)
print("Verschoben Kreis1:", k1.show())

k1.scale(0.5)
print("Vergrößert/Verkleinert um 0.5:", k1.show())

k2 = Circle(Point(1, 2), 0.8)
print("Kreis2:", k2.show())

print("Liegt Kreis2 in Kreis1?", k1.contains(k2))
print("Schneidet Kreis 1 mit Kreis2?", k2.intersects(k1))