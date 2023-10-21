from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
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


def plot_signal(indices1, samples1, indices2,samples2,result_sample, operation):
    plt.figure(figsize=(12, 10))
    plt.subplot(3, 1, 1)
    num_indices1= len(indices1)
    indices_new1 = np.linspace(0, num_indices1-1, num_indices1)
    spl = make_interp_spline(indices1, samples1, k=3)
    samples_new = spl(indices_new1)
    plt.plot(indices_new1, samples_new, color='green')
    plt.title("First signal")
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.grid(True)



    if operation=="addition":
        plt.subplot(3, 1, 2)
        num_indices2 = len(indices2)
        indices_new2 = np.linspace(0, num_indices2 - 1, num_indices2)
        spl = make_interp_spline(indices2, samples2, k=3)
        samples_new2 = spl(indices_new2)
        plt.plot(indices_new2, samples_new2, color='green')
        plt.title("Second signal")
        plt.xlabel("Sample Index")
        plt.ylabel("Amplitude")
        plt.grid(True)

        plt.subplot(3, 1, 3)
        num_indices3=len(indices1)
        indices_new3 = np.linspace(0,num_indices3-1,num_indices3)
        spl = make_interp_spline(indices1, result_sample, k=3)
        samples_new3 = spl(indices_new3)
        plt.plot(indices_new3, samples_new3, color='blue')
        plt.title("Addition of Signals")
        plt.xlabel("Sample Index")
        plt.ylabel("Amplitude")
        plt.grid(True)

        plt.tight_layout(pad=4.0)
        plt.show()

    elif operation=="subtraction":
        plt.subplot(3, 1, 2)
        num_indices2 = len(indices2)
        indices_new2 = np.linspace(0, num_indices2 - 1, num_indices2)
        spl = make_interp_spline(indices2, samples2, k=3)
        samples_new2 = spl(indices_new2)
        plt.plot(indices_new2, samples_new2, color='green')
        plt.title("Second signal")
        plt.xlabel("Sample Index")
        plt.ylabel("Amplitude")
        plt.grid(True)

        plt.subplot(3, 1, 3)
        num_indices3=len(indices1)
        indices_new3 = np.linspace(0,num_indices3-1,num_indices3)
        spl = make_interp_spline(indices1, result_sample, k=3)
        samples_new3 = spl(indices_new3)
        plt.plot(indices_new3, samples_new3, color='blue')
        plt.title("subtraction of Signals")
        plt.xlabel("Sample Index")
        plt.ylabel("Amplitude")
        plt.grid(True)

        plt.tight_layout(pad=4.0)
        plt.show()


    elif operation=="multiplication":
        plt.subplot(3, 1, 2)
        num_indices3=len(indices1)
        indices_new3 = np.linspace(0,num_indices3-1,num_indices3)
        spl = make_interp_spline(indices1, result_sample, k=3)
        samples_new3 = spl(indices_new3)
        plt.plot(indices_new3, samples_new3, color='blue')
        plt.title("multiblication of Signal")
        plt.xlabel("Sample Index")
        plt.ylabel("Amplitude")
        plt.grid(True)

        plt.tight_layout(pad=4.0)
        plt.show()

    elif operation=="Squaring":
        plt.subplot(3, 1, 2)
        num_indices3=len(indices1)
        indices_new3 = np.linspace(0,num_indices3-1,num_indices3)
        spl = make_interp_spline(indices1, result_sample, k=3)
        samples_new3 = spl(indices_new3)
        plt.plot(indices_new3, samples_new3, color='blue')
        plt.title("Squaring of Signal")
        plt.xlabel("Sample Index")
        plt.ylabel("Amplitude")
        plt.grid(True)

        plt.tight_layout(pad=4.0)
        plt.show()

def do_operation(operation,constant):

    if operation == "addition":
        file_path1 = load_file_path()
        if file_path1 != -1:
            indices1, samples1 = read_signal(file_path1)
        file_path2 = load_file_path()
        if file_path2 != -1:
            indices2, samples2 = read_signal(file_path2)
        selected_option = operation

        # Check if the two signals have the same length
        if len(samples1) != len(samples2):
            messagebox.showerror("Error", "The two signals must have the same length.")
            return
        # Add the samples of the two signals together
        result_add = [s1 + s2 for s1, s2 in zip(samples1, samples2)]
        plot_signal(indices1,samples1,indices2,samples2,result_add,selected_option)

    elif operation == "subtraction":
        file_path1 = load_file_path()
        if file_path1 != -1:
            indices1, samples1 = read_signal(file_path1)
        file_path2 = load_file_path()
        if file_path2 != -1:
            indices2, samples2 = read_signal(file_path2)
        selected_option = operation

        # Check if the two signals have the same length
        if len(samples1) != len(samples2):
            messagebox.showerror("Error", "The two signals must have the same length.")
            return
        result_sub= [s1 - s2 for s1, s2 in zip(samples1, samples2)]
        plot_signal(indices1,samples1,indices2,samples2,result_sub,selected_option)

    elif operation == "multiplication":
        file_path1 = load_file_path()
        if file_path1 != -1:
            indices1, samples1 = read_signal(file_path1)

        result_multi= [sample * float (constant) for sample in samples1]
        plot_signal(indices1,samples1,0,0,result_multi,operation)

    elif operation == "Squaring":
        file_path1 = load_file_path()
        if file_path1 != -1:
            indices1, samples1 = read_signal(file_path1)

        result_square = [sample ** 2 for sample in samples1]
        plot_signal(indices1, samples1, 0, 0, result_square, operation)