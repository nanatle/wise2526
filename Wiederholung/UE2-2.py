zahl1: int = 5
zahl2: int = 2

if zahl1 > zahl2:
    anfang = zahl2
    ende = zahl1

else:
    anfang = zahl1
    ende = zahl2

summe = sum(range(anfang, ende + 1))
print(summe)
