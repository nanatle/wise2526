import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        # private Attribute
        self.__x = x
        self.__y = y

    def distance(self, p):
        # Abstand zweier Punkte mit der Formel √((x2-x1)² + (y2-y1)²)
        dx = self.__x - p.__x
        dy = self.__y - p.__y
        return math.sqrt(dx*dx + dy*dy)

    def shift(self, x_val, y_val):
        # Punkt verschieben
        self.__x += x_val
        self.__y += y_val

    def show(self):
        # Koordinaten anzeigen
        return f"Point({self.__x}, {self.__y})"


class Circle:
    def __init__(self, x=0.0, y=0.0, radius=1.0):
        self.__center = Point(x, y)  # Mittelpunkt
        self.__radius = radius  # privater Radius

    def distance(self, obj):
        # Abstand von Kreis zum Punkt
        if isinstance(obj, Point):
            return self.__center.distance(obj) - self.__radius

        # Abstand von Kreis zu Kreis
        if isinstance(obj, Circle):
            center_dist = self.__center.distance(obj.__center)
            return center_dist - (self.__radius + obj.__radius)

    def shift(self, x_val, y_val):
        # Kreis verschieben → Mittelpunkt verschieben
        self.__center.shift(x_val, y_val)

    def scale(self, factor):
        # Radius vergrößern oder verkleinern
        self.__radius *= factor

    def contains(self, p):
        # Punkt liegt im Kreis wenn Abstand < Radius
        return self.__center.distance(p) <= self.__radius

    def intersect(self, c):
        # Zwei Kreise schneiden sich, wenn
        # Abstand der Mittelpunkte <= Summe der Radien
        center_dist = self.__center.distance(c.__center)
        return center_dist <= (self.__radius + c.__radius)

    def show(self):
        return f"Circle(center={self.__center.show()}, radius={self.__radius})"


print("--- TESTS ---\n")

# Punkt 1 (Standardwerte)
p1 = Point()
print("Punkt 1:", p1.show())

# Punkt 1 verschieben
p1.shift(2, 3)
print("Punkt 1 verschoben:", p1.show())

# Punkt 2 mit beliebigen Koordinaten
p2 = Point(5, 7)
print("Punkt 2:", p2.show())

# Abstand Punkt 1 – Punkt 2
print("Abstand p1 -> p2:", p1.distance(p2))

# Kreis 1 (Standardwerte)
c1 = Circle()
print("\nKreis 1:", c1.show())

# Kreis 1 verschieben
c1.shift(2, 3)
print("Kreis 1 verschoben:", c1.show())

# Kreis 1 skalieren
c1.scale(2)
print("Kreis 1 skaliert:", c1.show())

# Prüfen, ob Punkt 1 im Kreis 1 liegt
print("Punkt 1 in Kreis 1?", c1.contains(p1))

# Kreis 2 mit beliebigen Koordinaten
c2 = Circle(10, 3, 2)
print("\nKreis 2:", c2.show())

# Prüfen: Punkt 1 in Kreis 2?
print("Punkt 1 in Kreis 2?", c2.contains(p1))

# Prüfen: schneiden sich Kreis 1 und Kreis 2?
print("Schneiden sich Kreis 1 und Kreis 2?", c1.intersect(c2))