import numpy as np
import math as m
import matplotlib.pyplot as plt

from Tools.scripts.ndiff import fopen

"CONSTANTS"
c = 299792458
UPPER_GROUND_STATE_FRQ = 2.56300597908911 * (10 ** 9)
TRANS_FROM_GROUND_STATE = 384.2304844685 * (10 ** 12)


def wl_frq_unit_chnage(wl):
    return c / wl


def calculate_rydberg_wl_shanghai(frq):
    rydberg_transition = frq - TRANS_FROM_GROUND_STATE
    return  rydberg_transition


def read_Shanghai_text(file_name):
    data = np.empty((0, 2), float)
    with open(file_name) as f:
        for line in f:
            n = ""
            frq = ""
            i = 0
            while line[i] != " ":
                n = n + line[i]
                i = i + 1
            i = i + 1
            while (line[i] != "\n" and line[i]!= " "):
                frq = frq + line[i]
                i = i + 1
            row = [float(n),2* calculate_rydberg_wl_shanghai(float(frq) * m.pow(10, 12))]
            data = np.append(data, np.array([row]), axis=0)

    return (data[data[:, 0].argsort()]);


def read_Germany_text(file_name):
    data = np.empty((0, 2), float)
    with open(file_name) as f:
        for line in f:
            n = ""
            frq = ""
            i = 0
            while line[i] != " ":
                n = n + line[i]
                i = i + 1
            i = i + 1
            while line[i] != "(":
                frq = frq + line[i]
                i = i + 1
            row = [float(n),2*  float(frq) * m.pow(10, 12)]
            data = np.append(data, np.array([row]), axis=0)
    return (data)


def find_transition_of_n(data, n: int):
    for row in range(data.shape[0]):
        if data[row, 0] == n:
            return row
    return None


def single_plot(data, color, label, shape = "."):
    color_and_shape = color+shape
    starting_point= find_transition_of_n(data,40)
    plt.plot(data[starting_point:, 0], data[starting_point:, 1], color_and_shape, label=label)



def plots_87():
    single_plot(read_Shanghai_text("87\Shanghai_P(1_half)_transitions_87.txt"),"g","nP(1/2) states")

    single_plot(read_Shanghai_text("87\Shanghai_P(3_half)_transitions_87.txt"), "b", "nP(2/3) states")

    single_plot(read_Germany_text("87\Germany_5P_nD_3half_transitions.txt"), "r", "nD(3/2) states")

    single_plot(read_Germany_text("87\Germany_5P_nD_5half_transitions.txt"), "c", "nD(5/2) states")

    single_plot( read_Germany_text("87\Germany_5P_nS_half_transitions.txt"),color="m", label="nS(1/2) states")

    plt.legend()
    plt.show()


def single_calculation():
    print ("D(3/2)")
    data = read_Germany_text("87\Germany_5P_nD_3half_transitions.txt")
    print (data)
    print ("D(5/2)")
    data = read_Germany_text("87\Germany_5P_nD_5half_transitions.txt")
    print (data)
    print ("S(1/2)")
    data = read_Germany_text("87\Germany_5P_nS_half_transitions.txt")
    print(data)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    plots_87()
