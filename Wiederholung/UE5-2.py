#Zahl innerhalb eines Zahlenintervalls

def probe(zahl: int, xmin: int, xmax: int) -> bool:

    if zahl >= xmin and zahl <= xmax:
        return True

    else:
        return False


print(probe(2, 1, 5))