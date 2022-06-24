import matplotlib.pyplot as plt
import numpy as np


def nrzu_coder(data, amp=1):
    t = np.arange(0, len(data), .01)
    j = 1
    p = []
    for i in range(len(data) * 100):
        if t[i] < j:
            p.append(data[j - 1] * amp)
        else:
            p.append(data[j] * amp)
            j += 1

    plt.plot(t, p, color='k')
    plt.xlabel("Time in ms")
    plt.ylabel("Amplitude in Volts")
    plt.title("NRZ Unipolar")
    plt.show()
    return p


def nrzu_decoder(data):
    bits = [0]*(int(len(data)/100))
    idx = 0
    for i in range(0, len(data), 100):
        if data[i] > 0:
            bits[idx] = 1
        else:
            bits[idx] = 0
        idx += 1
    return bits


def psk_modulator(data, amp=1, freq=1000):
    bipolar = (2 * data - 1) * amp
    bit_duration = 1
    amplitude_scaling_factor = bit_duration / 2
    n_samples = 2000
    time = np.linspace(0, len(data), n_samples)

    samples_per_bit = n_samples / len(data)
    bb = np.repeat(bipolar, samples_per_bit)
    waveform = np.sqrt(2 * amplitude_scaling_factor / bit_duration) * np.cos(2 * np.pi * freq * time)
    bpsk_w = bb * waveform

    plt.plot(time, bpsk_w, color='k')
    plt.show()
    return bb, amp


def psk_demodulator(data, amp):
    bits = [0]*(int(len(data)/250))
    idx = 0
    for i in range(0, len(data), 250):

        if data[i] > 0:
            bits[idx] = 1
        else:
            bits[idx] = 0
        idx += 1

    if amp < 0:
        for i in range(0, len(bits)):
            if bits[i] > 0:
                bits[i] = 0
            else:
                bits[i] = 1
    return bits


bits = np.array([1, 0, 1, 1, 0, 0, 0, 1])
noise_constant = np.array([1, 1, 1, 1, 1, 1, 1, 1])
noise_random = np.array([np.random.randint(0, 2) for i in range(8)])

nrzu_signal = nrzu_coder(bits, amp=5)
print(nrzu_decoder(nrzu_signal))

psk_signal, amp = psk_modulator(bits, amp=2, freq=2000)
print(psk_demodulator(psk_signal, amp))

psk_signal, amp = psk_modulator(bits, amp=-2, freq=2000)
print(psk_demodulator(psk_signal, amp))
