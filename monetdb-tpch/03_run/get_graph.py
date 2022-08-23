
import numpy as np
from scipy import stats
from time import time
from matplotlib import style
import matplotlib.pyplot as plt
import csv
style.use('ggplot')

file_list =["SF-1.csv","SF-10.csv","SF-30.csv","SF-100.csv"]

def plot_TS_expect(result ,*name):  
    plt.figure(figsize=(16, 9))
    plt.xticks(np.arange(0, N+1, 500))
    plt.yticks(np.arange(0, 2, 0.05))
    plt.ylim(0, 1)
    for i in name:
        alpha = result[i][2][:, 1:]
        beta = result[i][3][:, 1:]
        plt.plot((alpha/(alpha+beta)))
    plt.title("Expected probability of each arm for "+" and ".join(name))
    plt.xlabel("time slot")
    plt.ylabel("expected probability")
    for i in name:
        plt.legend([j+" arm of "+i for i in name for j in ["1st", "2nd", "3rd"]])

def get_data(file_list):
    for file in file_list:
        f = open(file,"r")
        csv.DictReader(file)


get_data(file_list)
plot_TS_expect([1],)