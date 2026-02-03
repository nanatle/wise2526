def recursive_solution(x: int, schritt: int = 0) -> int:
    print(f"\nSchritt {schritt}: x = {x}")
    if x == 0:
        return 0

    if x == 1:
        return 1

    return x + recursive_solution(x - 1, schritt + 1)


def iterative_solution(x: int) -> int:
    schritt = 0
    f = 0
    for i in range(1, x + 1):
        schritt += 1
        f += i
    print(f"Anzahl der Schritte mit Iteration: {schritt}")
    return f


def second_recursion(x: float) -> float:
    if x <= 0:
        return 1

    return second_recursion(x - 1) + 2 * (second_recursion(x - 2))