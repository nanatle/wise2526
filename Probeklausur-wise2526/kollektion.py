#2.1

def l1():
    res1 = [(x + 1)**3 for x in range(-20, 23) if x % 2 == 0]
    return res1

print("Resultat 1: ", l1())


#2.2

def l2():
    res2 = [x**2 + 2 for x in range(-10, 12)]
    return res2

print("Resultat 2: ", l2())

#2.3

def d1() -> dict[int, int]:
    return dict(zip(l1(), l2()))

print("Dictionary: ", d1())


#2.4

import matplotlib.pyplot as plt
import numpy as np

def plot_list(l1_as_x: bool):
    x_data = np.array(l1())
    y_data = np.array(l2())

    if l1_as_x:
        x = x_data
        y = y_data
        plt.xlabel("l1")
        plt.ylabel("l2")
        plt.title("Plot von l2 von l1")

    else:
        x = y_data
        y = x_data
        plt.xlabel("l2")
        plt.ylabel("l1")
        plt.title("Plot von l1 gegen l2")

    plt.plot(x, y, "r")
    plt.show()

plot_list(True)
