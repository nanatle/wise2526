
def l1():
    res = [x ** 2 for x in range(-20, 23) if x % 2 == 0]
    return res


def l2() -> list[int]:
    menge = { (x + 1) ** 3 for x in range(-12, 12) }
    return menge


def d1() -> dict[int, int]:
    return dict(zip(l1(), l2()))

