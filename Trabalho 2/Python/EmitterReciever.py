import matplotlib.pyplot as plt
import numpy as np
import random as rnd
import binascii

local_path = "../CD_TestFiles/"
test_path = "../Test_Output/"


def nrzu_coder(data, amp=1.0):
    n = np.arange(0, len(data), .01)
    j = 1
    p = []
    for i in range(len(data) * 100):
        if n[i] < j:
            p.append(data[j - 1] * amp)
        else:
            p.append(data[j] * amp)
            j += 1

    plt.axis([0, len(data), -1, 6])
    plt.xticks(np.arange(0, len(data)+1, 20))
    plt.yticks(np.arange(-1, 7, 7))

    plt.plot(n, p, color='k')
    plt.xlabel("Time in ms")
    plt.ylabel("Amplitude in Volts")
    plt.title("NRZ Unipolar")
    plt.show()
    return p, amp


def nrzu_decoder(data, amp):
    amp = amp / 2
    data_bits = [0]*(int(len(data)/100))
    idx = 0
    for i in range(0, len(data), 100):
        if data[i] > amp:
            data_bits[idx] = 1
        else:
            data_bits[idx] = 0
        idx += 1
    return data_bits


def psk_modulator(data, amp=1.0, freq=1000):
    bipolar = (2 * data - 1) * amp
    bit_duration = 1
    amplitude_scaling_factor = bit_duration / 2
    n_samples = len(data)*2
    time = np.linspace(0, len(data), n_samples)

    samples_per_bit = n_samples / len(data)
    bb = np.repeat(bipolar, samples_per_bit)
    waveform = np.sqrt(2 * amplitude_scaling_factor / bit_duration) * np.cos(2 * np.pi * freq * time)
    bpsk_w = bb * waveform

    plt.axis([0, len(data), -3, 3])
    plt.xticks(np.arange(0, len(data) + 1, 20))
    plt.yticks(np.arange(-3, 4, 2))

    plt.plot(time, bpsk_w, color='k')
    plt.xlabel("Time in ms")
    plt.ylabel("Amplitude in Volts")
    plt.title("PSK")
    plt.show()
    return bb, amp


def psk_demodulator(data, amp):
    amp = amp / 2
    data_bits = [0]*(int(len(data)/2))
    idx = 0
    for i in range(0, len(data), 2):

        if data[i] > amp:
            data_bits[idx] = 1
        else:
            data_bits[idx] = 0
        idx += 1

    if amp < 0:
        for i in range(0, len(data_bits)):
            if data_bits[i] > 0:
                data_bits[i] = 0
            else:
                data_bits[i] = 1
    return data_bits


def calc_ber(original, received):
    error = 0.0
    size = len(original)
    for i in range(0, size):
        if original[i] != received[i]:
            error += 1
    return error / float(size)


# bits = np.array([1, 0, 1, 1, 0, 0, 0, 1])
with open(local_path + "a.txt", 'rb') as file:
    text = file.read()

t = bytearray(text)
h = binascii.hexlify(t)
b = bin(int(h, 16)).replace('b', '')
b = [int(i) for i in b]
bits = np.array(list(b))

# α = 1
noise_random = np.array([rnd.uniform(-1, 1) for i in range(len(bits))])

nrzu_signal, amplitude = nrzu_coder(bits + noise_random, amp=5)
nrzu_decoded = nrzu_decoder(nrzu_signal, amplitude)
print("BER: " + str(calc_ber(bits, nrzu_decoded)))

psk_signal, amplitude = psk_modulator(bits + noise_random, amp=2, freq=2000)
psk_decoded = psk_demodulator(psk_signal, amplitude)
print("BER: " + str(calc_ber(bits, psk_decoded)))

psk_signal, amplitude = psk_modulator(bits + noise_random, amp=-2, freq=2000)
psk_decoded = psk_demodulator(psk_signal, amplitude)
print("BER: " + str(calc_ber(bits, psk_decoded)))

# α = 0.5
noise_constant = np.array([1]*len(bits))*0.5

nrzu_signal, amplitude = nrzu_coder(bits + noise_constant, amp=5*0.5)
nrzu_decoded = nrzu_decoder(nrzu_signal, amplitude)
print("BER: " + str(calc_ber(bits, nrzu_decoded)))

psk_signal, amplitude = psk_modulator(bits + noise_constant, amp=2*0.5, freq=2000)
psk_decoded = psk_demodulator(psk_signal, amplitude)
print("BER: " + str(calc_ber(bits, psk_decoded)))

psk_signal, amplitude = psk_modulator(bits + noise_constant, amp=-2*0.5, freq=2000)
psk_decoded = psk_demodulator(psk_signal, amplitude)
print("BER: " + str(calc_ber(bits, psk_decoded)))
