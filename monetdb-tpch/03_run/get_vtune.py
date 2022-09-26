
from cProfile import label
import numpy as np
from scipy import stats
from time import time
from matplotlib import style
import matplotlib.pyplot as plt
import mpld3
from statistics import mean
import csv
from sympy import print_glsl

style.use('ggplot')

s = '{0}.sql-{1}-uarch.txt'
memory = [64, 8, 2]
query = range(1, 23)
formated_file_list = [s.format("{:0>2d}".format(j), i)
                      for i in memory for j in query]
metrics_list=["memory_bandwidth", "memory_latency",
               "core_bound", "memory_bound", "DRAM_bound","frontend_bound","bad_speculation","backend_bound"]
queue_list = ["q01", "q02", "q03", "q04", "q05", "q06", "q07", "q08", "q09", "q10",
              "q11", "q12", "q13", "q14", "q15", "q16", "q17", "q18", "q19", "q20", "q21", "q22", ]
result = np.zeros((8, 22, 3))
N = 100


def plot_TS_expect(*name):
    for i in range(0, 8):
        plt.figure(figsize=(16, 9))
        for j in range(0, 22):
            scaled_y = result[i][j]
            scaled_x = [64, 8, 2]
            plt.plot(scaled_x, scaled_y, label=queue_list[j])
        plt.legend(loc='upper left')
        plt.title("The graph for scaled "+name[i])
        plt.xlabel("quries")
        plt.ylabel("time")
        # plt.savefig(name[i]+".pdf", format='pdf')
        mpld3.save_html(plt, name[i]+".html")
        plt.close()


def get_data(file_list):
    for file_idx, file in enumerate(file_list):
        f = open(file, "r").readlines()
        tmp_bandwidth = []
        tmp_latency = []
        tmp_core = []
        tmp_memory = []
        tmp_dram = []
        tmp_front = []
        tmp_bad_spec = []
        print(file_idx % 22)
        print(file_idx//22)
        for line in f:
            if line.__contains__("Memory Bandwidth:"):
                try:
                    tmp_bandwidth.append(
                        float(line[34:39].replace(":", "").replace("%", "").strip()))
                except Exception as err:
                    print(err)
            if line.__contains__("Memory Latency:"):
                try:
                    tmp_latency.append(
                        float(line[32:37].replace(":", "").replace("%", "").strip()))
                except Exception as err:
                    print(err)
            if line.__contains__("Core Bound:"):
                try:
                    tmp_core.append(float(line[20:25].replace(
                        ":", "").replace("%", "").strip()))
                except Exception as err:
                    print(err)
            if line.__contains__("Memory Bound:"):
                try:
                    tmp_memory.append(float(line[22:27].replace(
                        ":", "").replace("%", "").strip()))
                except Exception as err:
                    print(err)
            if line.__contains__("DRAM Bound:"):
                try:
                    tmp_dram.append(float(line[23:28].replace(
                        ":", "").replace("%", "").strip()))
                except Exception as err:
                    print(err)
            if line.__contains__("Front-End Bound:"):
                try:
                    tmp_front.append(float(line[22:26].replace(
                        ":", "").replace("%", "").strip()))
                except Exception as err:
                    print(err)
            if line.__contains__("Bad Speculation:"):
                try:
                    tmp_front.append(float(line[21:25].replace(
                        ":", "").replace("%", "").strip()))
                except Exception as err:
                    print(err)
            if line.__contains__("Back-End Bound:"):
                try:
                    tmp_bad_spec.append(float(line[21:25].replace(
                        ":", "").replace("%", "").strip()))
                except Exception as err:
                    print(err)
            
        print(tmp_bandwidth)
        if (len(tmp_bandwidth)) == 0:
            result[0][file_idx % 22][file_idx//22] = 0.
            result[1][file_idx % 22][file_idx//22] = 0.
            result[2][file_idx % 22][file_idx//22] = 0.
            result[3][file_idx % 22][file_idx//22] = 0.
            result[4][file_idx % 22][file_idx//22] = 0.
            result[5][file_idx % 22][file_idx//22] = 0.
            result[6][file_idx % 22][file_idx//22] = 0.
        else:
            result[0][file_idx % 22][file_idx//22] = tmp_bandwidth[0]
            result[1][file_idx % 22][file_idx//22] = tmp_latency[0]
            result[2][file_idx % 22][file_idx//22] = tmp_core[0]
            result[3][file_idx % 22][file_idx//22] = tmp_memory[0]
            result[4][file_idx % 22][file_idx//22] = tmp_dram[0]
            result[5][file_idx % 22][file_idx//22] = tmp_front [0]
            result[6][file_idx % 22][file_idx//22] = tmp_bad_spec [0]

    return result


def plot_to_csv():
    with open('vtune.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([""]+queue_list)
        transposed = result.transpose(2, 0, 1)
        for idx,row in enumerate(transposed):  # [5,22,3]
            writer.writerow(["Memory Size"]+[str([2,8,64][idx])+"GB"]*22)
            for idx2,row2 in enumerate(row):
                writer.writerow([metrics_list[idx2]]+[a+"%" for a in row2.astype(str)])
    return


# print(formated_file_list)
result = get_data(formated_file_list)
plot_TS_expect(*metrics_list)
plot_to_csv()
