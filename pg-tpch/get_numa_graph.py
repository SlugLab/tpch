from cProfile import label
import numpy as np
from scipy import stats
from time import time
from matplotlib import style
import matplotlib.pyplot as plt
from statistics import mean
import csv
from sympy import print_glsl

style.use('ggplot')

s = 'SF-100-{0}.sql-numastat-{1}-{2}.txt'
memory = [6,8,10,12]
query = range(1, 23)
formated_file_list = [s.format("{:0>2d}".format(j), i,(idx+1)*0.5)
                      for idx,i in enumerate(memory) for j in query]
metrics_list=["memory_bandwidth", "memory_latency",
               "core_bound", "memory_bound", "DRAM_bound","frontend_bound","bad_speculation","backend_bound"]
queue_list = ["q01", "q02", "q03", "q04", "q05", "q06", "q07", "q08", "q09", "q10",
              "q11", "q12", "q13", "q14", "q15", "q16", "q17", "q18", "q19", "q20", "q21", "q22", ]
result = np.zeros((8, 22, 3))
N = 100

def draw_graph():
    for file in formated_file_list:
        tmp_line1 = []
        tmp_line2 = []
        tmp_time = []
        count = 0
        file_graph = str(file).replace(".txt", "")
        with open(file, 'r') as f:
            for line in f:
                if line.startswith("Total"):
                    tmp_line1.append(float(line[20:35].strip()))
                    tmp_line2.append(float(line[36:50].strip())+float(line[20:35].strip()))
                    tmp_time.append(count *0.005)
                    count+=1
        # print(tmp_line1)
        # print(tmp_time)
        plt.legend(loc='upper left')
        plt.plot(tmp_time, tmp_line1, label="local")
        plt.plot(tmp_time, tmp_line2, label="remote")
        plt.title("The graph for scaled "+file_graph)
        plt.xlabel("time")
        plt.ylabel("allocation (MB)")
        plt.savefig(file_graph+".pdf", format='pdf')
        plt.close()

draw_graph()