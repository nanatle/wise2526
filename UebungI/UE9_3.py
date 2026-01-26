from UE9_1 import Figur
from math import sqrt

class Polygon(Figur):
    def __init__(self, n: int, collection: list[int]):
        super().__init__("Polygon")
        self.n = n
        self._collection = collection

    def show(self) -> str:
        return f"{self.name}(Anzahl Seiten: {self.n}, die Seitenlänge: {self._collection})"

    def scale(self, faktor:float):
        for i in range(len(self._collection)):
            self._collection[i] += faktor

    def umfang(self) -> float:
        s = 0
        for i in range(len(self._collection)):
            s += self._collection[i]
        return s



class Dreieck (Polygon):
    def __init__(self, n: int, collection: list[int]):
        super().__init__(3, collection)
        self.name = "Dreieck"

    def ist_gleichseitig(self) -> bool:
        return self._collection[0] == self._collection[1] == self._collection[2]

    def ist_gleichschenklig(self) -> bool:
        return self._collection[0] == self._collection[1] or self._collection[1] == self._collection[2] or self._collection[0] == self._collection[2]

    def is_valid(self) -> bool:
        return (self._collection[0] + self._collection[1]) > self._collection[2] and (self._collection[0] + self._collection[2]) > self._collection[1] and (self._collection[1] + self._collection[2]) > self._collection[0]

    def flaeche(self) -> float:
        u = (self.umfang()) / 2
        return sqrt((u * (u - self._collection[0]) * (u - self._collection[1]) * (u - self._collection[2])))

    def umkreis_Radius(self) -> float:
        return (self._collection[0]*self._collection[1]*self._collection[2]) / (4*self.flaeche())




class Viereck(Polygon):

    def __init__(self, n: int, collection: list[int]):
        super().__init__(4, collection)
        self.name = "Viereck"

    def ist_Quadrat (self) -> bool:
        return self._collection[0] == self._collection[1] == self._collection[2] == self._collection[3]

    def ist_Rechteck (self) -> bool:
        return self._collection[0] == self._collection[2] and self._collection[1] == self._collection[3]

    def flaeche(self) -> float:
        if self.ist_Rechteck():
            return self._collection[0] * self._collection[1]
        else:
            return None

b1 = Polygon(4, [0, 1, 2, 3])
b1.scale(1)
print(b1.show())
print("Umfang von Polygon:", b1.umfang())

b2 = Dreieck(4, [1, 2, 3, 4])
#b2.scale(1.5)
print(b2.show())


b3 = Viereck(4, [2,3,4,5])
#b3.scale(1.5)
print(b3.show())
