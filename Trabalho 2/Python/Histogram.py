import matplotlib.pyplot as plt
import numpy as np


def histogram(filename):
    table = np.array([0]*256)
    with open(filename, 'rb') as file:
        text = file.read()
    text = np.array(list(text))
    for i in text:
        table[i] += 1

    plt.bar(np.arange(0, 256, 1), table)
    plt.show()

