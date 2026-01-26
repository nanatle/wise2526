from UE9_1 import Figur
from math import sqrt

class Polygon(Figur):
    def __init__(self, n: int, collection: list[int]):
        super().__init__("Polygon")
        self.n = n
        self._collection = collection

    def show(self):
        return f"{self.name}(Anzahl Seiten: {self.n}, die Seitenlänge: {self._collection})"

    def scale(self, faktor:float):
        for i in range(len(self._collection)):
            self._collection[i] += faktor

    def umfang(self):
        s = 0
        for i in range(len(self._collection)):
            s += self._collection[i]
        return s



class Dreieck (Polygon):
    def ist_gleichseitig(self):
        return self._collection[0] == self._collection[1] == self._collection[2]

    def ist_gleichschenklig(self):
        return self._collection[0] == self._collection[1] or self._collection[1] == self._collection[2] or self._collection[0] == self._collection[2]

    def is_valid(self):
        return (self._collection[0] + self._collection[1]) > self._collection[2] and (self._collection[0] + self._collection[2]) > self._collection[1] and (self._collection[1] + self._collection[2]) > self._collection[0]

    def flaeche(self):
        u = (self.umfang()) / 2
        return sqrt((u * (u - self._collection[0]) * (u - self._collection[1]) * (u - self._collection[2])))

    def umkreis_Radius(self):
        return (self._collection[0]*self._collection[1]*self._collection[2]) / (4*self.flaeche())




class Viereck(Polygon):
    def ist_Quadrat (self):
        return self._collection[0] == self._collection[1] == self._collection[2] == self._collection[3]

    def ist_Rechteck (self):
        return self._collection[0] == self._collection[2] and self._collection[1] == self._collection[3]

    def flaeche(self):
        if self.ist_Rechteck():
            return self._collection[0] * self._collection[1]
        else:
            return None