from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from tkinter import messagebox
import random


def load_file_path():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path != "":
        return file_path
    else:
        return -1


def read_signal(file_path):
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
                V2 = float(L[1])
                samples.append(V2)
                line = f.readline()
            else:
                break
    return  samples


def load_one_signal():
    file_path1 = load_file_path()
    if file_path1 != -1:
         samples_1 = read_signal(file_path1)
    return  samples_1


def quantize(num_bits, is_bits):
    signal = load_one_signal();

    # Step 1: Find min and max amplitude
    min_val = min(signal)
    max_val = max(signal)
    if is_bits==True:
      num_levels = 2 ** num_bits
    else:
        num_levels=num_bits

    # Step 2: Find delta
    delta = (max_val - min_val) / num_levels

    # Step 3: Make ranges
    ranges = np.arange(min_val, max_val, delta)

    # Step 4: Calculate mid point for each range
    mid_points = ranges[:-1] + delta / 2

    # Step 5: Quantize
    quantized_signal = np.zeros_like(signal)
    interval_numbers = np.zeros_like(signal)
    for i in range(len(signal)):
        interval_number = np.argmin(np.abs(mid_points - signal[i]))
        quantized_signal[i] = mid_points[interval_number]
        interval_numbers[i] = int(interval_number + 1)

    # Step 6: Calculate mse
    error = quantized_signal - signal
    squared_error = error ** 2

    # Step 7: Encode interval numbers to binary
    binary_encoded_intervals = [format(int(interval), 'b') for interval in interval_numbers]
    print(quantized_signal, error, interval_numbers, binary_encoded_intervals)
    return quantized_signal, error, interval_numbers, binary_encoded_intervals

