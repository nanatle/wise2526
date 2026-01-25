import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes()
ax.spines.left.set_position('zero')
ax.spines.bottom.set_position('zero')


def plotter(function, min_x = -5, max_x = 5, step = 0.1):
    x = np.arange(min_x, max_x, step)
    y = function(x)
    plt.plot(x, y)
    plt.show()

if __name__ == "__main__":
    plotter(lambda x: x * x, (-5), 5, 0.1)
    plotter(lambda x: np.sin(x), 0, 10, 0.1)