from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline



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
    plt.title("Discrete Form")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid(True)
    
    # Subplot 2: Continuous
    plt.subplot(1, 2, 2)

    # Generate a curve using interpolation for smoothness (optional)
    if(use_interpolation):
        indices_new = np.linspace(min(indices), max(indices), 100) 
        spl = make_interp_spline(indices, samples, k = 3)
        samples_new = spl(indices_new) 
        plt.plot(indices_new , samples_new, color='green')  
    else:
        plt.plot(indices, samples, color='green')  

    plt.title("Continuous Form")
    plt.xlabel("Time")
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

def compute_signal(amplitude, wave_type, analogue_frequency, sampling_frequency, phase_shift):
    print(amplitude)
    print(wave_type)
    print(analogue_frequency)
    print(sampling_frequency)
    print(phase_shift)


def generate_signal():
    print("needs implementation")

def compare_outputs():
    print("needs implementation")