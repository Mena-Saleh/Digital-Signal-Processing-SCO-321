import cmath
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from tkinter import messagebox
import random
import math


# Test functions (given)

# Use to test the Amplitude of DFT and IDFT
def SignalComapreAmplitude(SignalInput = [] ,SignalOutput= []):
    if len(SignalInput) != len(SignalInput):
        return False
    else:
        for i in range(len(SignalInput)):
            A=round(SignalInput[i])
            B=round(SignalOutput[i])
            if abs(A-B)>0.001:
                return False
            elif A!=B:
                return False
        return True

# Use to test the PhaseShift of DFT
def SignalComaprePhaseShift(SignalInput = [] ,SignalOutput= []):
    if len(SignalInput) != len(SignalInput):
        return False
    else:
        for i in range(len(SignalInput)):
            A=round(SignalInput[i])
            B=round(SignalOutput[i])
            if abs(A-B)>0.0001:
                return False
            elif A!=B:
                return False
        return True


# Helper functions

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
                V1 = float(L[0])
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

def plot_frequency_domain_signal(frequency, amplitude, phase_shift):

    plt.figure(figsize=(12, 6)) 
    # Subplot 1: Frequency vs amplitude
    plt.subplot(1, 2, 1)
    plt.bar(frequency, amplitude, width = 2) 

    plt.title('Frequency vs Amplitude')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    
    # Subplot 2: Frequency vs phase_shift
    plt.subplot(1, 2, 2)
    plt.bar(frequency, phase_shift, color='green', width = 2)

    # Horizontal line at y=0
    plt.axhline(y=0, color='black', linewidth=1)

    plt.title('Frequency vs Phase')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Phase (radians)')
    plt.grid(True)

    plt.tight_layout(pad=4.0)
    plt.show()

    plt.show()

def save_frequency_domain_signal(file_path, amplitude, phase_shift, file_name_end = "_Frequency_Domain.txt" ):
    with open(file_path[:-4] + file_name_end, 'w') as f:
        f.writelines('0\n')
        f.writelines('1\n')
        f.writelines(str(len(amplitude)) + '\n')
        for i in range(len(amplitude)):
            f.write(str(amplitude[i]) + ' ' + str(phase_shift[i]) + '\n')

def plot_time_domain_signal(indices, samples):

    plt.figure(figsize=(6, 6)) 

    # Scatter plot
    plt.scatter(indices, samples) 

    # Draw vertical lines from each point to the x-axis
    plt.vlines(indices, 0, samples, linestyles='dashed')

    # Horizontal line at y=0
    plt.axhline(y=0, color='black', linewidth=1)

    plt.title("Discrete Form")
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.grid(True)

    plt.show()

def save_time_domain_signal(file_path, samples):
    with open(file_path[:-4] + '_Time_Domain.txt', 'w') as f:
        f.writelines('0\n')
        f.writelines('0\n')
        f.writelines(str(len(samples)) + '\n')
        for i in range(len(samples)):
            f.write(str(i) + ' ' + str(samples[i].real) + '\n')

# Custom compare functions

def compare_DFT_result(your_amplitude, your_phase_shift):
    amplitude, phase_shift, file_path = load_signal()
    if SignalComapreAmplitude(amplitude, your_amplitude) & SignalComaprePhaseShift(phase_shift, your_phase_shift):
        print("Success")
        messagebox.showinfo("success", "Test case passed successfully")
    else:
        print("Failed")

def compare_IDFT_result(your_amplitude):
    indices, amplitude, load_file_path = load_signal()
    if SignalComapreAmplitude(amplitude, your_amplitude):
        print("Success")
        messagebox.showinfo("success", "Test case passed successfully")
    else:
        print("Failed")

# Logic functions

def compute_fourier_transform(samples, isIDFT = False):
    N = len(samples)
    result = []
    for k in range(N):
        sum = 0
        for n in range(N):
            if isIDFT:
                sum += samples[n] * cmath.exp(1j *2* cmath.pi * k * n / N)
            else:
                sum += samples[n] * cmath.exp(-1j *2* cmath.pi * k * n / N)
        if isIDFT:
            result.append(sum/N)
        else:
            result.append(sum)
    return result

def compute_frequency_amplitude_phase_shift(sampling_frequency, DFT_result):

    # Calculate amplitude and phase
    amplitude = []
    phase_shift = []

    for x in DFT_result:
        amplitude.append(math.sqrt(x.real ** 2 + x.imag ** 2))
        phase_shift.append(math.atan2(x.imag, x.real))

    # Calculate the frequency for each sample
    frequency = []
    N = len(DFT_result)
    fundamental_frequency = round(( 2 * cmath.pi * int(sampling_frequency) ) / N)

    for i in range(N):
        frequency.append(int((i+1) * fundamental_frequency))

    return frequency, amplitude, phase_shift

def polar_to_cartesian(amplitude, phase_shift):
    cartesian_points = []
    for i, k in zip(amplitude, phase_shift):
        x = i * cmath.cos(k)  # Real part
        y = i * cmath.sin(k)  # Imaginary part
        cartesian_point = x + (y * 1j)  # Final complex number
        cartesian_points.append(cartesian_point)
    return cartesian_points


# Main functions that call other functions


def domain_transform(sampling_frequency, isDFT):
    if isDFT:
        # Input validation
        if sampling_frequency == "":
            messagebox.showerror("error", "please enter sampling frequency.")
            return
        sampling_frequency = int(sampling_frequency)

        # Loading signal
        indices, samples, file_path = load_signal()

        # Applying DFT
        DFT_result = compute_fourier_transform(samples)
        frequency, amplitude, phase_shift = compute_frequency_amplitude_phase_shift(sampling_frequency, DFT_result)

        # Printing results
        print("frequency: ", frequency)
        print("amplitude: ", amplitude)
        print("phase_shift: ", phase_shift)

        # Plotting and saving to file
        plot_frequency_domain_signal(frequency, amplitude, phase_shift)
        save_frequency_domain_signal(file_path, amplitude, phase_shift)
        
        # Comparing results to file
        compare_DFT_result(amplitude, phase_shift)

    else:
        # Loading signal
        amplitude, phase_shift, file_path = load_signal()

        # Signal conversion and applying IDFT
        cartesian_points = polar_to_cartesian(amplitude, phase_shift)
        IDFT_result = compute_fourier_transform(cartesian_points, isIDFT= True)
        indices = np.arange(len(IDFT_result))
        IDFT_result = [round(x.real,2) for x in IDFT_result]

        # Printing results
        print("IDFT_result: ", IDFT_result)

        # Plotting and saving to file
        plot_time_domain_signal(indices, IDFT_result)
        save_time_domain_signal(file_path, IDFT_result)

        # Comparing results to file
        compare_IDFT_result(IDFT_result)


def modify_components(index, new_amplitude, new_phase_shift):

    index = int(index)
    new_amplitude = float(new_amplitude)
    new_phase_shift = float(new_phase_shift)

    # Loading signal
    amplitude, phase_shift, file_path = load_signal()
    N = len(amplitude)
    if (index > N):
        messagebox.showerror("Error", "Index out of bounds.")
        return
    
    # Saving old values
    old_amplitude = amplitude[index]
    old_phase_shift = phase_shift[index]

    # Changing amplitude components
    amplitude = [new_amplitude if abs(value - old_amplitude) < 0.01 else value for value in amplitude]

    # Changing phase shift components
    for i in range (N):
        if abs(abs(phase_shift[i]) - old_phase_shift) < 0.01:
            phase_shift[i] = math.copysign(1, phase_shift[i]) * new_phase_shift

    # Saving to file
    save_frequency_domain_signal(file_path, amplitude, phase_shift, file_name_end = "_Modified.txt")
    messagebox.showinfo("success", "Signal modified and saved to file successfully.")


