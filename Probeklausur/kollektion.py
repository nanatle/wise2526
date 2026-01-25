
def l1():
    return [x**2 for x in range(-20,23) if x % 2 == 0]

def l2() -> list[int]:
    return [(x+1)**3 for x in range(-10,12) ]

def d1() -> dict[int, int]:
    list1 = l1()
    list2 = l2()
    return dict(zip(list1, list2))

l1()
#print(l1())
l2()
#print(l2())
d1()
#print(d1())