#Zahl ist Primzahl?

def prime(zahl: int) -> bool:

    if zahl <= 1:
        return False


    for i in range(2, int(zahl ** 0.5) + 1):
        if zahl % i == 0:
            return False

    return True


print(prime(11))
