import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return 1 + 3 * x

def f2(x, a, b):
    return a + b * x

A: int = 0
B: int = 1

def f3(x, a = A, b = B):
    return a + b * x

def f4(x, a):
    s = 0
    for i in range(len(a)):
        s += a[i] * (x**i)
    return s


def main():
    x_max = 10
    x_min = 0
    xdata = np.arange (x_min, x_max,0.1)
    ydata1 = f1(xdata)
    plt.plot (xdata, ydata1, color = "red")

    ydata2 = f2(xdata, x_min, x_max)
    plt.plot (xdata, ydata2, color = "blue")

    ydata3 = f3(xdata, 0, 1)
    plt.plot (xdata, ydata3, color = "green")

    ydata4 = f4(xdata, (12.05, 0, 1, 3, 0, 0, 7))
    plt.plot (xdata, ydata4, color = "pink")

    plt.title('my function')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

if __name__ == '__main__':
    main()
