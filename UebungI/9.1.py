#Parent-Klasse: geometrische Figur

class Figur :
    def __init__(self) :
        self.name = ""

    def show(self) :
        print(self.name)

    def scale(self, faktor:float):
        self.name = faktor

import math

class Punkt(Figur):
    def __init__(self, x: float = 0, y: float = 0):
        super().__init__()
        self._x = x
        self._y = y

  
    def shift(self, x_val, y_val):
        self._x += x_val
        self._y += y_val

    def show(self):
        return f"Punkt({self._x}, {self._y})"


objF = Figur()
objF.show()
objF.scale(10)
objP = Punkt()
objP.distance(objF)
objP.shift(10, 20)
objP.show()