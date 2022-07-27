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
    return wl_frq_unit_chnage(rydberg_transition)


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
            while line[i] != "\n":
                frq = frq + line[i]
                i = i + 1
            row = [float(n), wl_frq_unit_chnage(calculate_rydberg_wl_shanghai(float(frq) * m.pow(10, 12)))]
            data = np.append(data, np.array([row]), axis=0)
            print(n)
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
            row = [float(n), float(frq) * m.pow(10, 12)]
            data = np.append(data, np.array([row]), axis=0)
    return (data)


def find_transition_of_n(data, n: int):
    for row in range(data.shape[0]):
        if data[row, 0] == n:
            return data[row, :]
    return None




def plots():
    P_1half = read_Shanghai_text("Shanghai_P(1_half)_transitions_87.txt")
    #plt.plot(P_1half[:, 0], P_1half[:, 1], "g", label="nP(1/2) states")

    P_3half = read_Shanghai_text("Shanghai_P(3_half)_transitions_87.txt")
    #plt.plot(P_3half[:, 0], P_3half[:, 1], "b", label="nP(2/3) states")

    #plt.legend()
    #plt.show()


def single_calculation():
    a = 624.4597844 * 10 ** 12
    b = 1008.6719549 * 10 ** 12

    b = wl_frq_unit_chnage(calculate_rydberg_wl_shanghai(b))
    print(a)
    print(b)
    print((a - b) * 10 ** (-9))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    plots()
