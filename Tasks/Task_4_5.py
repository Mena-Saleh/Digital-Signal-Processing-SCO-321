import cmath
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox
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
    plt.bar(frequency, amplitude, width = 0.5) 

    plt.title('Frequency vs Amplitude')
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    plt.grid(True)

    
    # Subplot 2: Frequency vs phase_shift
    plt.subplot(1, 2, 2)
    plt.bar(frequency, phase_shift, color='green', width = 0.5)

    # Horizontal line at y=0
    plt.axhline(y=0, color='black', linewidth=1)

    plt.title('Frequency vs Phase shift')
    plt.xlabel('Frequency')
    plt.ylabel('Phase shift (radians)')
    plt.grid(True)

    plt.tight_layout(pad=4.0)
    plt.show()

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

def plot_old_and_modified_signals(indices, amplitude_old, phase_shift_old, amplitude_new, phase_shift_new):
    
    plt.figure(figsize=(12, 6)) 
    # Subplot 1: Indices vs amplitude (OLD)
    plt.subplot(2, 2, 1)
    plt.bar(indices, amplitude_old, width = 0.5) 

    plt.title('Indices vs Amplitude [OLD]')
    plt.xlabel('Indices')
    plt.ylabel('Amplitude')
    plt.grid(True)

    
    # Subplot 2: Indices vs phase_shift (OLD)
    plt.subplot(2, 2, 2)
    plt.bar(indices, phase_shift_old, color='green', width = 0.5)

    # Horizontal line at y=0
    plt.axhline(y=0, color='black', linewidth=1)

    plt.title('Indices vs Phase shift [OLD]')
    plt.xlabel('Indices')
    plt.ylabel('Phase shift (radians)')
    plt.grid(True)

    # Subplot 3: Indices vs amplitude (NEW)
    plt.subplot(2, 2, 3)
    plt.bar(indices, amplitude_new, width = 0.5, color = 'orange') 

    plt.title('Indices vs Amplitude [NEW]')
    plt.xlabel('Indices')
    plt.ylabel('Amplitude')
    plt.grid(True)

    
    # Subplot 4: Indices vs phase_shift (NEW)
    plt.subplot(2, 2, 4)
    plt.bar(indices, phase_shift_new, color='yellow', width = 0.5)

    # Horizontal line at y=0
    plt.axhline(y=0, color='black', linewidth=1)

    plt.title('Indices vs Phase shift [NEW]')
    plt.xlabel('Indices')
    plt.ylabel('Phase shift (radians)')
    plt.grid(True)



    plt.tight_layout(pad=4.0)
    plt.show()

def save_frequency_domain_signal(file_path, amplitude, phase_shift, file_name_end = "_Frequency_Domain_DFT.txt" ):
    with open(file_path[:-4] + file_name_end, 'w') as f:
        f.writelines('0\n')
        f.writelines('1\n')
        f.writelines(str(len(amplitude)) + '\n')
        for i in range(len(amplitude)):
            f.write(str(amplitude[i]) + ' ' + str(phase_shift[i]) + '\n')

def save_time_domain_signal(file_path, samples, file_name_end = "_Time_Domain_IDFT.txt", m = -1):
    with open(file_path[:-4] + file_name_end, 'w') as f:
        f.writelines('0\n')
        f.writelines('0\n')
        f.writelines(str(len(samples)) + '\n')
        if m == -1:
            for i in range(len(samples)):
                f.write(str(i) + ' ' + str(samples[i].real) + '\n')
        else:
            for i in range(m):
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

def compute_discrete_fourier_transform(samples, isIDFT = False):
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

def compute_discrete_cosine_transform(samples):
    N = len(samples)
    result = []
    for k in range(N):
        sum = 0
        for n in range(N):
            sum += samples[n] * math.cos( (math.pi/(4*N)) * (2*n-1) * (2*k-1) )
        result.append(math.sqrt(2/N) * sum)
    return result

def remove_dc_component_time_domain(samples):
    result = samples - np.mean(samples)
    return result

def remove_dc_component_frequency_domain(samples):
    # Applying DFT
    DFT_result = compute_discrete_fourier_transform(samples)
    # Removing DC
    DFT_result[0] = 0
    # Applying IDFT
    IDFT_result = compute_discrete_fourier_transform(DFT_result, isIDFT= True)
    IDFT_result = [round(x.real,2) for x in IDFT_result]
    return IDFT_result

# Main functions that call other functions


def domain_transform(user_input, transformation_method, ):

    if(user_input):
        user_input = int(user_input)

    # DFT
    if transformation_method == 0:
        # Input validation
        if user_input == "":
            messagebox.showerror("error", "please enter sampling frequency.")
            return

        # Loading signal
        indices, samples, file_path = load_signal()

        # Applying DFT
        DFT_result = compute_discrete_fourier_transform(samples)
        frequency, amplitude, phase_shift = compute_frequency_amplitude_phase_shift(user_input, DFT_result)

        # Printing results
        print("frequency: ", frequency)
        print("amplitude: ", amplitude)
        print("phase_shift: ", phase_shift)

        # Plotting and saving to file
        plot_frequency_domain_signal(frequency, amplitude, phase_shift)
        save_frequency_domain_signal(file_path, amplitude, phase_shift)
        
        # Comparing results to file
        compare_DFT_result(amplitude, phase_shift)

    # IDFT
    elif transformation_method == 1:
        # Loading signal
        amplitude, phase_shift, file_path = load_signal()

        # Signal conversion and applying IDFT
        cartesian_points = polar_to_cartesian(amplitude, phase_shift)
        IDFT_result = compute_discrete_fourier_transform(cartesian_points, isIDFT= True)
        indices = np.arange(len(IDFT_result))
        IDFT_result = [round(x.real,2) for x in IDFT_result]

        # Printing results
        print("IDFT result: ", IDFT_result)

        # Plotting and saving to file
        plot_time_domain_signal(indices, IDFT_result)
        save_time_domain_signal(file_path, IDFT_result)

        # Comparing results to file
        compare_IDFT_result(IDFT_result)
    # DCT
    else:
        if user_input == "":
            messagebox.showerror("error", "please enter sampling frequency.")
            return
        # Loading signal
        indices, samples, file_path = load_signal()

        # Applying DCT
        DCT_result = compute_discrete_cosine_transform(samples)

        # Printing results
        print("DCT result: ", DCT_result)

        # Plotting and saving to file
        plot_time_domain_signal(indices, DCT_result)
        save_time_domain_signal(file_path, DCT_result,  '_Frequency_Domain_DCT.txt', m = user_input)

        # Comparing results to file
        compare_IDFT_result(DCT_result)


def modify_components(index, new_amplitude_value, new_phase_shift_value):

    index = int(index)
    new_amplitude_value = float(new_amplitude_value)
    new_phase_shift_value = float(new_phase_shift_value)

    # Loading signal
    amplitude, phase_shift, file_path = load_signal()
    N = len(amplitude)
    if (index > N):
        messagebox.showerror("Error", "Index out of bounds.")
        return
    
    # Saving old values
    old_amplitude_value = amplitude[index]
    old_phase_shift_value = phase_shift[index]

    # Changing amplitude components
    amplitude_modified = [new_amplitude_value if abs(value - old_amplitude_value) < 0.01 else value for value in amplitude]

    # Changing phase shift components
    phase_shift_modified = phase_shift.copy()
    for i in range (N):
        if abs(abs(phase_shift[i]) - old_phase_shift_value) < 0.01:
            phase_shift_modified[i] = math.copysign(1, phase_shift[i]) * new_phase_shift_value
            

    # Saving to file
    save_frequency_domain_signal(file_path, amplitude_modified, phase_shift_modified, file_name_end = "_Modified.txt")
    messagebox.showinfo("success", "Signal modified and saved to file successfully.")

    # Comparing old and new signals in a plot
    indices = range(N)
    plot_old_and_modified_signals(indices, amplitude, phase_shift, amplitude_modified, phase_shift_modified)


def remove_dc_component(is_frequency_domain):

    # Loading signal
    indices, samples, file_path = load_signal()
    
    # Remove DC component
    if(is_frequency_domain):
        result = remove_dc_component_frequency_domain(samples)
    else:
        result = remove_dc_component_time_domain(samples)

    # Print results
    print("Signal after removing DC component: ", result)

    # Plotting and saving to file
    plot_time_domain_signal(indices, result)
    save_time_domain_signal(file_path, result , '_DC_component_removed.txt')

    # Comparing results to file
    compare_IDFT_result(result)

