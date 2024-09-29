import matplotlib.pyplot as plt
import numpy as np


def plot():
    x = np.linspace(-10, 10, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()
    # xpoints = np.array([1, 8])
    # ypoints = np.array([3, 10])

    # plt.plot(xpoints, ypoints)
    # plt.show()