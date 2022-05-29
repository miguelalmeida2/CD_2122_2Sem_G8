import numpy as np
import matplotlib.pyplot as plot
from scipy import signal


def nrzu_coder(data: list):
    for bit in data:
        if bit:
            print(1)
        else:
            print(0)


def psk_modulator(data: list):
    n = 10


# Sampling rate 1000 hz / second
t = np.linspace(0, 10, 1000, endpoint=True)

bits = list([0])*1000
time = 0

for i in range(0, len(bits)):
    y = 5 * np.pi * (time / 0.001)
    if y >= 1:
        bits[i] = 1
    else:
        bits[i] = 0
    time += 1

# Plot the square wave signal
plot.plot(t, bits)

# Give x axis label for the square wave plot
plot.xlabel('Time')

# Give y axis label for the square wave plot
plot.ylabel('Amplitude')
plot.grid(True, which='both')

# Provide x axis and line color
plot.axhline(y=0, color='k')

# Set the max and min values for y axis
plot.ylim(-2, 2)

# Display the square wave drawn
plot.show()
