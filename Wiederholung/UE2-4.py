z: str = str(input("Ihre beliebig lange Reihe von Ziffern 0 - 9: "))

zahl: str = " ".join(z)
print("Ihre Reihe:", zahl)

l1 = list(map(int, zahl.split()))
print(l1)
summe = sum(l1)
print(summe)

