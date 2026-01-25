#Plotting
#Functions

import matplotlib.pylot as plt
import numpy as np

def f1(x):
    return 1 + 3 * x

def f2(x, a, b):
    return a + b * x

A: int = 0
B: int = 1

def f3(x, a = A, b = B):
    return a +b * x

def f4(x, a):
    sum = 0
    for i in range(len(a)):
        sum += a[i] * x[i]
    return sum


def main():
    x = np.arange (0,10,0.01)
#    y = f(x)

    plt.plot (x, f1(x))
    plt.plot (x, f2(x, 2, 3))
    plt.plot (x, f3(x))
    plt.plot (x, f4(x, 12.05, 0, 1, 3, 0, 0, 7))
    plt.title('my function')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

if __name__ == '__main__':
    main()

