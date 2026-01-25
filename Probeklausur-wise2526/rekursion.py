#3.1 Funktion Implementierung

def recursive_solution(x: int, schritt: int = 0) -> int:
    print(f"Schritt {schritt}: x = {x}")

    if x == 1:
        return 1

    return x**2 + recursive_solution(x - 1, schritt + 1)

print("Ergebnis 1: ",recursive_solution(3, schritt = 1))



#3.2 Iterative Umwandlung

def iterative_solution(x: int) -> int:
    f = 1

    while x > 1:
        f += x**2
        x -= 1

    return f

print("-------\nErgebnis 2: ",iterative_solution(3))



#3.3 Doppelte Rekursion

def second_recursion(n: float) -> float:
    if n <= 0:
        return 1

    return second_recursion(n - 1) + 2*second_recursion(n - 2)

print("-------\nErgebnis 3: ",second_recursion(3))

