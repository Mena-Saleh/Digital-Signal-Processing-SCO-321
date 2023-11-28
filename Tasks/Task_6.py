import cmath
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox

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
                V2 = float(L[1])
                indices.append(V1)
                samples.append(V2)
                line = f.readline()
            else:
                break
    return indices, samples

def load_signal():
    file_path = load_file_path()
    if file_path != -1:
        indices, samples = read_signal(file_path)
    return indices, samples, file_path

def plot_smoothed_signal(indices,samples,smoothed_indices,smoothed_samples,window_size):
    plt.figure(figsize=(8, 5))
    plt.subplot(2, 1, 1)
    plt.plot(indices, samples, label='Original Signal')
    plt.title('Original Signal')
    plt.xlabel('Index')
    plt.ylabel('Sample Value')
    plt.legend()

    # Plot the smoothed signal
    plt.subplot(2, 1, 2)
    plt.plot(smoothed_indices, smoothed_samples, label=f'Smoothed Signal (Window Size={window_size})', color='orange')
    plt.title(f'Smoothed Signal (Window Size={window_size})')
    plt.xlabel('Index')
    plt.ylabel('Sample Value')
    plt.legend()
    plt.tight_layout()

    # Show the plots
    plt.show()

def smooth_signal(window_size):
    window_size= int(window_size)
    indices, samples, load_file_path = load_signal()
    smoothed_samples=[]
    smoothe_signal_len=len(samples) - window_size + 1
    for i in range(smoothe_signal_len):
        window = samples[i:i + window_size]
        avg = sum(window) / window_size
        smoothed_samples.append(avg)
    smoothed_indices = []
    for i in range(len(smoothed_samples)):
        smoothed_indices.append(indices[i])

    #ploting
    plot_smoothed_signal(indices,samples,smoothed_indices,smoothed_samples,window_size)


