import numpy as np
import math as m
import matplotlib.pyplot as plt

from Tools.scripts.ndiff import fopen

"CONSTANTS"
c = 299792458
UPPER_GROUND_STATE_FRQ = 2.56300597908911*(10**9)
TRANS_FROM_GROUND_STATE =  384.2304844685 * (10**12)

def wl_frq_unit_chnage(wl):
    return c/wl

def calculate_rydberg_wl_shanghai(frq):
    rydberg_transition = frq - TRANS_FROM_GROUND_STATE

    return (rydberg_transition)


def read_Shanghai_text():
    data = np.empty((0,2), float)
    with open ("Shanghai_P_transitions.txt") as f:
        for line in f:
            n = ""
            frq = ""
            i = 0
            while line [i] !=" ":
                n = n+ line[i]
                i=i+1
            i=i+1
            while line [i] !=" ":
                frq = frq + line[i]
                i=i+1
            row = [float(n), calculate_rydberg_wl_shanghai(float(frq)*m.pow(10,12))]
            data = np.append(data, np.array([row]), axis=0)
    return (data);

def read_Germany_text(file_name):
    data = np.empty((0,2), float)
    with open (file_name) as f:
        for line in f:
            n = ""
            frq = ""
            i = 0
            while line [i] !=" ":
                n = n+ line[i]
                i=i+1
            i=i+1
            while line [i] !="(":
                frq = frq + line[i]
                i=i+1
            row = [float(n), float(frq)*m.pow(10,12)]
            data = np.append(data, np.array([row]), axis=0)
    return (data);

def find_transition_of_n (data,n: int):
    for row in range(data.shape[0]):
        if data[row, 0] ==n:
            return data[row,:]
    return None



# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    data_nshalf =  read_Germany_text("Germany_5P_nS_half_transitions.txt")
    #plt.plot (data_nshalf[:, 0], data_nshalf[:, 1], label="nS(1/2) states")

    data_nD_3half =read_Germany_text("Germany_5P_nD_3half_transitions.txt" )
    #plt.plot (data_nD_3half[:,0], data_nD_3half[:,1], label= "nD 3/2 states")

    obsereved_line= find_transition_of_n(data_nD_3half, 51)
    print(obsereved_line)
    base_frq = obsereved_line[1]

    dataSh = read_Shanghai_text()
    plt.plot(dataSh[:, 0], dataSh[:, 1]-base_frq, label="nP(2/3) states")


    data_nD_5half = read_Germany_text("Germany_5P_nD_5half_transitions.txt")
    #plt.plot(data_nD_5half[:, 0], data_nD_5half[:, 1], label="nD 5/2 states")
    plt.legend()
    plt.show()

