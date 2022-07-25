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
    print (rydberg_transition)
    return (wl_frq_unit_chnage(rydberg_transition))


def read_Shanghai_text():
    data = np.empty((0,2), float)
    with open ("Shanghai_P_transitions.txt") as f:
        for line in f:
            n = ""
            frq = ""
            i = 0
            while line [i] !=" ":
                n = n+ line[i]
                i=i+1;
            i=i+1
            while line [i] !=" ":
                frq = frq + line[i]
                i=i+1
            row = [float(n), calculate_rydberg_wl_shanghai(float(frq)*m.pow(10,12))]
            data = np.append(data, np.array([row]), axis=0)
    return (data);

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = read_Shanghai_text()
    plt.plot (data[:,0], data[:,1])
    plt.show()
