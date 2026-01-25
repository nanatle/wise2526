#2.1

def l1():
    res1 = [(x + 1)**3 for x in range(-20, 23) if x % 2 == 0]
    return res1

print("Resultat 1: ", l1())


#2.2

def l2():
    res2 = [x**2 + 2 for x in range(-11, 12)]
    return res2

print("Resultat 2: ", l2())

#2.3

def d1() -> dict[int, int]:
    return dict(zip(l1(), l2()))

print("Dictionary: ", d1())
