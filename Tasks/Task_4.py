import cmath
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from tkinter import messagebox
import random
import math


def load_file_path():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path != "":
        return file_path
    else:
        return -1


def read_signal(file_path):
    indices = []
    samples = []

    with open(file_path, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            L = line.strip()
            if len(L.split(' ')) == 2:
                L = line.split(' ')
                V1 = int(L[0])
                V2 = int(L[1])
                indices.append(V1)
                samples.append(V2)
                line = f.readline()
            else:
                break
    return indices, samples

def load_one_signal():
    file_path = load_file_path()
    if file_path != -1:
        indices, samples = read_signal(file_path)
    return indices, samples


def DFT():
    indices, samples = load_one_signal()
    N = len(samples)
    result = []
    for k in range(N):
        sum = 0
        for n in range(N):
            sum += indices[n] * cmath.exp(-1j *2* cmath.pi * k * n / N)
        result.append(sum)
    return result, samples


def freq_domain(sample_freq, is_dft):
    if(is_dft==True):
        dft_result,samples = DFT()
    amplitude = []
    phase = []
    # Calculate amplitude and phase
    for x in dft_result:
        amplitude.append(math.sqrt(x.real ** 2 + x.imag ** 2))
        phase.append(math.atan2(x.imag, x.real))

        # Calculate the frequency for each sample
    freq = []
    N = len(samples)
    first_freq = round(( 2 * cmath.pi * int(sample_freq) ) / N)
    for i in range(N):
      freq.append(int((i+1) * first_freq))
    print(amplitude)
    print(freq)
    print(phase)

        # Plot frequency vs amplitude
    plt.figure()
    plt.bar(freq, amplitude,width=0.2)
    plt.title('Frequency vs Amplitude')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')

        # Plot frequency vs phase
    plt.figure()
    plt.bar(freq, phase,width=0.2)
    plt.title('Frequency vs Phase')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Phase (radians)')

    plt.show()

    return amplitude, phase






