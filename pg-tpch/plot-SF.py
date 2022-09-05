import numpy as np
from scipy import stats
from time import time
from matplotlib import style
import matplotlib.pyplot as plt
import csv
style.use('ggplot')


queue_list = ["q01","q02","q03","q04","q05","q06","q07","q08","q09","q10","q11","q12","q13","q14","q15","q16","q17","q18","q19","q20","q21","q22",]
result = np.zeros((22,4))
f = open("SF.csv","r")
res = csv.DictReader(f)
for i in range(4):
    for r_idx,r in enumerate(res):
        result[r_idx][i]=int(r['rss'])

for i in range(0,3):
    print(i)
    plt.figure(figsize=(16, 9))

    for j in range(0,22):
        scaled_y = result[i][j]
        scaled_x = [1,10,30,100]
        print(scaled_y)
        plt.plot(scaled_x, scaled_y,label=queue_list[j])
    leg = plt.legend(loc='upper left')
    plt.title("The graph for scaled "+name[i])
    plt.xlabel("SF")
    plt.ylabel("times")
    plt.savefig(name[i]+".pdf", format='pdf')
    plt.close()
