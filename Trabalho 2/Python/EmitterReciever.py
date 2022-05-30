import matplotlib.pyplot as plt
import numpy as np


def nrzu_coder(data: list):
    for bit in data:
        if bit:
            print(1)
        else:
            print(0)


def psk_modulator(data: list):
    n = 10


b = [np.random.randint(0, 2) for i in range(2500)]
t = np.arange(0, 25, .01)
j = 1
p = []
for i in range(2500):
    if t[i] < j:
        p.append(b[j-1])
    else:
        p.append(b[j])
        j += 1

plt.plot(t, p, color='k')
plt.xlabel("Time")
plt.ylabel("Value")
plt.title("NRZ Unipolar")
plt.show()


