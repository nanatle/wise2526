zahl: int = int(input("Gebe eine ganzzahlige positive Zahl ein: "))

teiler: int = 2
print("Primzahlzerlegung von ", zahl, "=", end=" ")

"""while zahl > 1:
    if zahl % teiler == 0:
        print(teiler, end = " ")
        zahl = zahl // teiler
        if zahl > 1:
            print("* ", end="")
    else:
        teiler += 1"""



print("\n effizienter --------------")

while teiler * teiler <= zahl:
    while zahl % teiler == 0:
        print(teiler, end=" ")
        zahl //= teiler
        if zahl > 1:
            print("* ", end="")
    teiler += 1

if zahl > 1:
    print(zahl)
