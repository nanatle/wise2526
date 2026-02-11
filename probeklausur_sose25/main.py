from kollektion import *
from rekursion import recursive_solution, iterative_solution, second_recursion
from parser import parse_weight, normalize, add


def menue():
    print("\n")
    print("***Welcome to Probeklausur***")
    print("\n")
    print("Which option would you like to choose?")
    print("\n (a) Kollektion/Tupel"
          "\n (b) Rekursion"
          "\n (c) Parser"
          "\n (d) Exit")

    print("\n")


def a():

    print("List 1 = ", l1())
    print("List 2 =", l2())
    print("Dict = ", d1())


def b():

    zahl = int(input("Geben Sie eine ganze Zahl ein: "))
    print("Rekursion: ", recursive_solution(zahl, 1))
    print("Iteration: ", iterative_solution(zahl))

    print("\nDoppelte Rekursion bei n = 9: ", second_recursion(9))


def c():

    print(parse_weight("23.5 kg"))
    print(normalize(parse_weight("23.5 kg"), "g"))
    print(add("136 g", "5.109 kg"))


while True:
    menue()
    wahl = str(input("Please enter your choice: "))

    if wahl == "a":
        a()
    elif wahl == "b":
        b()
    elif wahl == "c":
        c()
    elif wahl == "d":
        print("Exited.")
        break
    else:
        print("Ungültige Eingabe.")