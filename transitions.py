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


def read_Shanghai_text(file_name, scale='wl'):
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
            value = calculate_rydberg_wl_shanghai(float(frq) * m.pow(10, 12))
            if scale == 'wl':
                value = wl_frq_unit_chnage(value)
            row = [float(n), value]
            data = np.append(data, np.array([row]), axis=0)

    return (data[data[:, 0].argsort()]);


def read_Germany_text(file_name, scale='wl'):
    '''
    :param file_name: The file contining the information, written in germany style.
    :param scale: 'wl' for wavelength, 'frq' for Hrz.
    :return: data in numpy array form
    '''

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
            value = float(frq) * m.pow(10, 12)
            if scale == 'wl':
                value = wl_frq_unit_chnage(value)

            row = [float(n),value]
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
    #plt.plot(data[starting_point:, 0], data[starting_point:, 1], color_and_shape, label=label)
    plt.plot(data[starting_point:, 0], data[starting_point:, 1], color_and_shape, label=label)



def plots_87(scale = 'frq'):
    single_plot(read_Shanghai_text("87\Shanghai_P(1_half)_transitions_87.txt",scale),"g","nP(1/2) states")

    single_plot(read_Shanghai_text("87\Shanghai_P(3_half)_transitions_87.txt",scale), "b", "nP(2/3) states")

    single_plot(read_Germany_text("87\Germany_D_3half_transitions.txt",scale), "r", "nD(3/2) states")

    single_plot(read_Germany_text("87\Germany_D_5half_transitions.txt",scale), "c", "nD(5/2) states")

    single_plot( read_Germany_text("87\Germany_S_half_transitions.txt",scale),color="m", label="nS(1/2) states")

    plt.legend()
    plt.show()

def read_any_file(file_name,scale= 'wl'):
    data_mat = None
    format = file_name[3]  # shows if germany or Shanghai
    if format == 'G':
        data_mat = read_Germany_text(file_name, format)
    elif format == 'S':
        data_mat = read_Shanghai_text(file_name, format)
    return (data_mat)


def find_near_transitions(data_file_name, n):
    '''
    :param data: file to take data from
    :param n: n energy level
    :param Germany_or_Shanghai 'G' for Germany format, 'S' for Shanghai
    :return: plot a graph and returns data of all near transitions
    '''
    given_data_files =["87\Shanghai_P(1_half)_transitions_87.txt","87\Shanghai_P(3_half)_transitions_87.txt",
                       "87\Germany_D_3half_transitions.txt","87\Germany_D_5half_transitions.txt",
                       "87\Germany_S_half_transitions.txt"]

    this_data = read_any_file(data_file_name,'frq')
    this_frq = this_data[find_transition_of_n(this_data, n)][1]


    colors=["r","g","b","y","p"]
    c=0
    for file_name in given_data_files:
        if file_name !=data_file_name:
            data_mat=read_any_file(file_name, 'frq')
            data_mat[:,1]=data_mat[:,1]-this_frq
            data_label = file_name.split("_")[1]+" "+file_name.split("_")[2]
            single_plot(data_mat,colors[c], data_label)
            c=c+1
            print(data_label)
            print(data_mat)
    plt.legend()
    plt.show()


def single_calculation():
    x = np.linspace(0, 20, 1000)
    y = np.sin(x)


    plt.plot(x, y, "-b", label="sine")

    y = np.cos(x)
    plt.plot(x, y, "-r", label="cosine")
    plt.legend(loc="upper left")
    plt.ylim(-1.5, 2.0)
    plt.show()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #find_near_transitions("87\Germany_S_half_transitions.txt",56)
    plots_87('frq')
    #P3half= (1008.6155556*10**12-TRANS_FROM_GROUND_STATE)/10**12
    #print(P3half)
    #D3half = 624.459
    #print (P3half-D3half)
