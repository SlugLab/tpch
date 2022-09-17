
from cProfile import label
import numpy as np
from scipy import stats
from time import time
from matplotlib import style
import matplotlib.pyplot as plt
from statistics import mean

from sympy import print_glsl

style.use('ggplot')

s = 'SF-100-{0}.sql-wss-{1}.txt'
memory = [2**i for i in range(0,7)]
query = range(1,23)
formated_file_list = [s.format("{:0>2d}".format(j),i) for i in memory for j in query]

queue_list = ["q01","q02","q03","q04","q05","q06","q07","q08","q09","q10","q11","q12","q13","q14","q15","q16","q17","q18","q19","q20","q21","q22",]
result=np.zeros((5,22,7))
N=100


def plot_TS_expect(*name):
    i=0
    plt.figure(figsize=(16, 9))
    plt.ylim([0,20000])
    for j in range(0,22):
        scaled_y = result[i][j][::-1]
        scaled_x = [2**i for i in range(0,7)]
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
        tmp_rss = []
        tmp_wss = []
        tmp_ref = []
        tmp_time = []
        print (file_idx%22)
        print (file_idx//22)
        for line in f:
            try:
                tmp_wss.append(float(line[21:31].strip()))
                tmp_rss.append(float(line[10:20].strip()))
                tmp_time.append(float(line[0:10].strip()))
                tmp_ref.append(float(line[32:42].strip()))
            except Exception as err:
                print(err)
        # print(tmp_rss)
        if (len(tmp_rss)) == 0:
            result[0][file_idx%22][file_idx//22]=2**(file_idx//22)
            result[1][file_idx%22][file_idx//22]=2**(file_idx//22)
            result[2][file_idx%22][file_idx//22]=2**(file_idx//22)
            result[3][file_idx%22][file_idx//22]=2**(file_idx//22)
            result[4][file_idx%22][file_idx//22]=99999999
        else:
            result[0][file_idx%22][file_idx//22]=max(tmp_rss)
            result[1][file_idx%22][file_idx//22]=mean(tmp_rss)
            result[2][file_idx%22][file_idx//22]=max(tmp_wss)
            result[3][file_idx%22][file_idx//22]=mean(tmp_wss)
            result[4][file_idx%22][file_idx//22]=sum(tmp_time)
        # result[3][r_idx][file_idx]=int(r['llc_miss'])/int(r['llc_hit'])
    return result


result = get_data(formated_file_list)
plot_TS_expect("time_query")