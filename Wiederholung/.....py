#4.1
class Block:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def isCorrect(self) -> bool:
        return self.a > 0 and self.b > 0 and self.c > 0

b1 = Block(2.2, 1.2, 3.2)
b1.isCorrect()
print("Sind die Kantenlänge a, b und c positiv?", b1.isCorrect())

#4.2
class Quader(Block):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def volumen(self) -> float:
        volumen = self.a * self.b * self.c
        print("Volumen von Quader:", volumen)
        return volumen

    def oberflaeche(self) -> float:
        oberflaeche = 2 * (self.a * self.b + self.a * self.c)
        print("Oberfläche von Quader:", oberflaeche)
        return oberflaeche

b2 = Quader(2.0,1.0, 3.0)
b2.volumen()
b2.oberflaeche()

#4.3
class Barren(Quader):
    def __init__(self,a, b, c, name: str, density: float):
        super().__init__(a,b,c)
        self.name = name
        self.density = density

    def masse(self) -> float:
        Masse = self.a * self.b * self.c * self.density
        print("Masse von Barren aus", self.name, ":", Masse, "g/cm^3")
        return Masse

b3 = Barren(2.0,1.0, 3.0, name="PVC", density=1.5)
b3.masse()