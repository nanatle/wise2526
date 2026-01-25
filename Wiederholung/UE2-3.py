zahl: int = int(input("vierstellige Zahl eingeben: "))
z: str = str(zahl).zfill(4)

print("Ihre Zahl besteht aus:")
print(z[0], "Tausender")
print(z[1], "Hunderter")
print(z[2], "Zehner")
print(z[3], "Einser")





