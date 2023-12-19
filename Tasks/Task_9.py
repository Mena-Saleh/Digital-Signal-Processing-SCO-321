import cmath
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox
import math
from Tasks import Task_4_5 as tsk4
from Tasks import Task_6_7_8 as tsk8


def ConvTest(Your_indices, Your_samples):
    """
    Test inputs
    InputIndicesSignal1 =[-2, -1, 0, 1]
    InputSamplesSignal1 = [1, 2, 1, 1 ]

    InputIndicesSignal2=[0, 1, 2, 3, 4, 5 ]
    InputSamplesSignal2 = [ 1, -1, 0, 0, 1, 1 ]
    """

    expected_indices = [-2, -1, 0, 1, 2, 3, 4, 5, 6]
    expected_samples = [1, 1, -1, 0, 0, 3, 3, 2, 1]

    if (len(expected_samples) != len(Your_samples)) and (len(expected_indices) != len(Your_indices)):
        print("Conv Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_indices)):
        if (Your_indices[i] != expected_indices[i]):
            print("Conv Test case failed, your signal have different indicies from the expected one")
            return
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print("Conv Test case failed, your signal have different values from the expected one")
            return
    print("Conv Test case passed successfully")
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
        line1 = int(f.readline())  # Strip to remove leading/trailing whitespaces

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
    return indices, samples, line1
def load_two_signals():

    # Read two signals
    file_path1 = load_file_path()
    if file_path1 != -1:
        indices_1, samples_1,len1 = read_signal(file_path1)
    file_path2 = load_file_path()
    if file_path2 != -1:
        indices_2, samples_2,len2 = read_signal(file_path2)
    # Check if the two signals have the same length
    return indices_1, samples_1, indices_2, samples_2,len1,len2

def compute_frequency_amplitude_phase_shift( DFT_result):

    # Calculate amplitude and phase
    amplitude = []
    phase_shift = []

    for x in DFT_result:
        amplitude.append(math.sqrt(x.real ** 2 + x.imag ** 2))
        phase_shift.append(math.atan2(x.imag, x.real))


    return  amplitude, phase_shift

def fast_conv():
    indices_1, samples_1, indices_2, samples_2,len1,len2= load_two_signals()
    N1 = len1
    N2 = len2
    padded_signal1 = np.pad(samples_1, (0, N1 + N2 - 1 - N1), 'constant')
    padded_signal2 = np.pad(samples_2, (0, N1 + N2 - 1 - N2), 'constant')
    #num_new_indices_sig1 = len(padded_signal1) - N1
    #num_new_indices_sig2 = len(padded_signal2) - N2

    # Generate new indices by extending the existing ones
    #last_index_sig1 = indices_1[-1]
    #last_index_sig2=indices_2[-1]
   # new_indices_sig1 = indices_1 + list(range(last_index_sig1 + 1, last_index_sig1 + 1 + num_new_indices_sig1))
    #new_indices_sig2=indices_2 + list(range(last_index_sig2 + 1, last_index_sig2 + 1 + num_new_indices_sig2))


    DFT_sig1= tsk4.compute_discrete_fourier_transform(padded_signal1)
    DFT_sig2 = tsk4.compute_discrete_fourier_transform(padded_signal2)


    result_indices, result_signal = tsk8.convolve_signals(indices_1,DFT_sig1,indices_2,DFT_sig2)

    #compute idft
    amplitude, phase_shift = compute_frequency_amplitude_phase_shift(result_signal)
    cartesian_points = tsk4.polar_to_cartesian(amplitude, phase_shift)
    IDFT_result = tsk4.compute_discrete_fourier_transform(cartesian_points, isIDFT=True)
    IDFT_result = [round(x.real, 2) for x in IDFT_result]
    ConvTest(result_indices,IDFT_result)
    print("res values",IDFT_result)


