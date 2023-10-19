from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox
from scipy.interpolate import make_interp_spline


# Evaluation function (given):

def signal_samples_are_equal(file_name,indices,samples):
    expected_indices=[]
    expected_samples=[]
    with open(file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L=line.strip()
            if len(L.split(' '))==2:
                L=line.split(' ')
                V1=int(L[0])
                V2=float(L[1])
                expected_indices.append(V1)
                expected_samples.append(V2)
                line = f.readline()
            else:
                break
                
    if len(expected_samples)!=len(samples):
        print("Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(expected_samples)):
        if abs(samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print("Test case failed, your signal have different values from the expected one") 
            return
    print("Test case passed successfully")

# Part 1: Browsing signals and displaying them:

def load_file_path():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path != "":
        return file_path
    else:
        return -1
    
def read_signal(file_path):
    indices=[]
    samples=[]

    with open(file_path, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            L=line.strip()
            if len(L.split(' '))==2:
                L=line.split(' ')
                V1=int(L[0])
                V2=float(L[1])
                indices.append(V1)
                samples.append(V2)
                line = f.readline()
            else:
                break
    
    return indices, samples

def plot_signal(indices, samples, use_interpolation = True):

    plt.figure(figsize=(12, 6)) 

    # Subplot 1: Discrete
    plt.subplot(1, 2, 1)
    plt.scatter(indices, samples) 

    # Draw vertical lines from each point to the x-axis
    plt.vlines(indices, 0, samples, linestyles='dashed')

    plt.title("Discrete Form")
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.grid(True)

    
    # Subplot 2: Continuous
    plt.subplot(1, 2, 2)

    # Generate a curve using interpolation for smoothness (optional)
    if(use_interpolation):
        indices_new = np.linspace(min(indices), max(indices), max(indices) * 20) 
        spl = make_interp_spline(indices, samples, k = 3)
        samples_new = spl(indices_new) 
        plt.plot(indices_new , samples_new, color='green')  
    else:
        plt.plot(indices, samples, color='green')  

    plt.title("Continuous Form")
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.grid(True)

    plt.tight_layout(pad=4.0)
    plt.show()
    
def browse_signal():
    file_path = load_file_path()
    if file_path != -1:
        indices, samples = read_signal(file_path)
        plot_signal(indices, samples)

# Part 2: Generating signals and displaying them:

def check_input_if_empty(amplitude, wave_type, analogue_frequency, sampling_frequency, phase_shift):
    if(amplitude == "" or wave_type == "" or analogue_frequency == "" or sampling_frequency == "" or phase_shift == ""):
        messagebox.showerror("Error", "One or more fields are missing, please fill them all.")

def compute_signal(amplitude, wave_type, analogue_frequency, sampling_frequency, phase_shift):
    amplitude = int(amplitude)
    analogue_frequency = int(analogue_frequency)
    sampling_frequency = int(sampling_frequency)
    phase_shift = float(phase_shift)

    if (sampling_frequency <= 0):
        messagebox.showerror("Error", "Sampling frequency must be greater than 0.")
        return

    if(sampling_frequency < 2*analogue_frequency):
        messagebox.showerror("Error", "Sampling frequency must be greater than or equal twice that of the analogue frequency.")
        return
    
    indices = np.arange(sampling_frequency)
    samples_time = np.linspace(0,1,sampling_frequency)
    normalized_frequency = analogue_frequency/sampling_frequency
    
    if(wave_type == "sin"):
        samples = amplitude * np.sin(2 * np.pi * normalized_frequency * indices + phase_shift)
    else:
        samples = amplitude * np.cos(2 * np.pi * normalized_frequency * indices + phase_shift)
    

    return samples_time, indices, samples

def generate_signal(amplitude, wave_type, analogue_frequency, sampling_frequency, phase_shift):
    check_input_if_empty(amplitude, wave_type, analogue_frequency, sampling_frequency, phase_shift)
    samples_time, indices, samples = compute_signal(amplitude, wave_type, analogue_frequency, sampling_frequency, phase_shift)
    plot_signal(indices[:40], samples[:40], False)

def compare_outputs(amplitude, wave_type, analogue_frequency, sampling_frequency, phase_shift):
    check_input_if_empty(amplitude, wave_type, analogue_frequency, sampling_frequency, phase_shift)
    samples_time, indices, samples = compute_signal(amplitude, wave_type, analogue_frequency, sampling_frequency, phase_shift)
    file_path = load_file_path()
    signal_samples_are_equal(file_path, indices, samples)
