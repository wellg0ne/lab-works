import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1, 1, 0.001)
y = 2 * np.sin(np.pi * x * 3)


if __name__ == '__main__':
    plt.plot(x, y)
    plt.show()
