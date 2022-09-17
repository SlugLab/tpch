
from cProfile import label
import numpy as np
from scipy import stats
from time import time
from matplotlib import style
import matplotlib.pyplot as plt
from statistics import mean

from sympy import print_glsl

style.use('ggplot')

s = '{0}.sql-{1}-uarch.txt'
memory = [64,8,2]
query = range(1,23)
formated_file_list = [s.format("{:0>2d}".format(j),i) for i in memory for j in query]

queue_list = ["q01","q02","q03","q04","q05","q06","q07","q08","q09","q10","q11","q12","q13","q14","q15","q16","q17","q18","q19","q20","q21","q22",]
result=np.zeros((2,22,3))
N=100


def plot_TS_expect(*name):
    for i in range(0,2):
        plt.figure(figsize=(16, 9))
        for j in range(0,22):
            scaled_y = result[i][j]
            scaled_x = [64,8,2]
            plt.plot(scaled_x, scaled_y,label=queue_list[j])
        plt.legend(loc='upper left')
        plt.title("The graph for scaled "+name[i])
        plt.xlabel("quries")
        plt.ylabel("time")
        plt.savefig(name[i]+".pdf", format='pdf')
        plt.close()

def get_data(file_list):
    for file_idx,file in enumerate(file_list):
        f = open(file,"r").readlines()
        tmp_bandwidth = []
        tmp_latency = []
        print (file_idx%22)
        print (file_idx//22)
        for line in f:
            if line.__contains__("Memory Bandwidth:"):
                try:
                    tmp_bandwidth.append(float(line[34:39].replace(":","").replace("%","").strip()))
                except Exception as err:
                    print(err)
            if line.__contains__("Memory Latency:"):
                try:
                    tmp_latency.append(float(line[32:37].replace(":","").replace("%","").strip()))
                except Exception as err:
                    print(err)
        print(tmp_bandwidth)
        if (len(tmp_bandwidth)) == 0:
            result[0][file_idx%22][file_idx//22]=0.
            result[1][file_idx%22][file_idx//22]=0.
        else:
            result[0][file_idx%22][file_idx//22]=tmp_bandwidth[0]
            result[1][file_idx%22][file_idx//22]=tmp_latency[0]
    return result


# print(formated_file_list)
result = get_data(formated_file_list)
plot_TS_expect("memory_bandwidth","memory_latency")