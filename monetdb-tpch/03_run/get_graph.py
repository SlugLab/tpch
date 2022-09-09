
import numpy as np
from scipy import stats
from time import time
from matplotlib import style
import matplotlib.pyplot as plt
import csv
style.use('ggplot')

file_list =["SF-1.csv","SF-10.csv","SF-30.csv","SF-100.csv"]
queue_list = ["q01","q02","q03","q04","q05","q06","q07","q08","q09","q10","q11","q12","q13","q14","q15","q16","q17","q18","q19","q20","q21","q22",]
result=np.zeros((17,22,4))
N=100

def plot_TS_expect(*name):  
    plt.figure(figsize=(16, 9))
    # plt.xticks(np.arange(0, N+1, 10))
    # plt.yticks(np.arange(0, N+1, 10))
    # plt.ylim(0, 1)
    for i in range(0,3):
        print(i)
        plt.figure(figsize=(16, 9))

        for j in range(0,22):
            first_scale = result[i][j][0]
            scaled_y = [item/first_scale for item in result[i][j] ]
            scaled_x = [1,10,30,100]
            plt.plot(scaled_x, scaled_y,label=queue_list[j])
        leg = plt.legend(loc='upper left')
        plt.title("The graph for scaled "+name[i])
        plt.xlabel("SF")
        plt.ylabel("times")
        plt.savefig(name[i]+".pdf", format='pdf')
        plt.close()
    for i in range(3,9):
        plt.figure(figsize=(16, 9))

        print(i)
        for j in range(0,22):
            scaled_y = result[i][j]
            scaled_x = [1,10,30,100]
            print(scaled_y)
            plt.plot(scaled_x, scaled_y,label=queue_list[j])
        leg = plt.legend(loc='upper left')
        plt.title("The graph for scaled "+name[i])
        plt.xlabel("SF")
        plt.ylabel("percentage")
        plt.savefig(name[i]+".pdf", format='pdf')
        plt.close()
    for i in range(9,14):
        plt.figure(figsize=(16, 9))

        print(i)
        for j in range(0,22):
            scaled_y = result[i][j]
            scaled_x = [1,10,30,100]
            print(scaled_y)
            plt.plot(scaled_x, scaled_y,label=queue_list[j])
        leg = plt.legend(loc='upper left')
        plt.title("The graph for scaled "+name[i])
        plt.xlabel("SF")
        plt.ylabel("MB")
        plt.savefig(name[i]+".pdf", format='pdf')
        plt.close()


def get_data(file_list):
    for file_idx,file in enumerate(file_list):
        f = open(file,"r")
        res = csv.DictReader(f)
        for r_idx,r in enumerate(res):
            result[0][r_idx][file_idx]=int(r['rss'])
            # result[1][r_idx][file_idx]=int(r['avgrss'])
            result[2][r_idx][file_idx]=int(r['vsz'])
            result[3][r_idx][file_idx]=int(r['llc_miss'])/int(r['llc_hit'])
            result[4][r_idx][file_idx]=int(r['llc_hitm'])/int(r['llc_hit'])
            result[5][r_idx][file_idx]=int(r['llc_miss_stat'])/(int(r['llc_lookup_stat'])+int(r['llc_hitm_stat'])+int(r['llc_hit_stat'])+int(r['llc_miss_stat']))
            result[6][r_idx][file_idx]=int(r['llc_hitm_stat'])/(int(r['llc_lookup_stat'])+int(r['llc_hitm_stat'])+int(r['llc_hit_stat'])+int(r['llc_miss_stat']))
            result[7][r_idx][file_idx]=int(r['llc_miss_stat'])/(int(r['llc_hitm_stat'])+int(r['llc_hit_stat'])+int(r['llc_miss_stat']))
            result[8][r_idx][file_idx]=int(r['llc_hitm_stat'])/(int(r['llc_hitm_stat'])+int(r['llc_hit_stat'])+int(r['llc_miss_stat']))
            result[9][r_idx][file_idx]=float(r['maxrss'])
            # result[10][r_idx][file_idx]=float(r['avgrss1'])
            result[11][r_idx][file_idx]=float(r['maxwss'])
            # result[12][r_idx][file_idx]=float(r['avgwss'])
            result[13][r_idx][file_idx]=float(r['ref'])
            result[14][r_idx][file_idx]=float(r['maxref_s'])
            result[15][r_idx][file_idx]=float(r['avgref_s'])
    return result


result = get_data(file_list)
plot_TS_expect("rss","avgrss","vsz","llc_miss_rate","llc_hitm_rate","llc_miss_stat_rate","llc_hitm_stat_rate","llc_miss_stat_shared_rate","llc_hitm_stat_shared_rate","maxrss","avgrss1","maxwss","avgwss","ref",'maxref_s','avgref')