#4.1 Block--------------

class Block:
    def __init__(self):
        self.a = 2.0
        self.b = 1.0
        self.c = 3.2

    def isCorrect(self) -> bool:
        return self.a > 0 and self.b > 0 and self.c > 0

b1 = Block()
b1.isCorrect()
print("Sind die Kantenlängen a, b und c positiv? -", b1.isCorrect())

#4.2 Quader-----------

class Quader(Block):
    def __init__(self):
        super().__init__()

    def flaeche(self) -> float:
        oberflaeche = 2 * (self.a * self.b + self.a * self.c + self.a * self.b)
        print("Oberfläche von Quader: ", oberflaeche)

    def volumen(self) -> float:
        volumen = self.a * self.b + self.b * self.c
        print("Volumen von Quader: ", volumen)

b2 = Quader()
b2.flaeche()
b2.volumen()

#4.3 Barren--------
class Barren(Quader):
    def __init__(self, name: str, density: float):
        super().__init__()
        self.name = name
        self.density = density

    def masse(self) -> float:
        gewicht = self.a * self.b * self.c * self.density
        print("Masse von Barren aus", self.name,": (", self.a, "*", self.b, "*", self.c, ") *", self.density, " = ", gewicht)

b3 = Barren("PVC", 1.5)
b3.masse()

