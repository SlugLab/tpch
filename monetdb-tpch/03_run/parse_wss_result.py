import os

import numpy as np
from statistics import mean

rss=[]
wss=[]
ref=[]

for item in sorted(os.listdir("./")):
    if str(item).endswith("wss-1.txt"):
        f= open(item,'r')
        lines = f.readlines()
        tmp_rss = []
        tmp_wss = []
        tmp_ref = []
        for line in lines:
            try:
                tmp_rss.append(float(line[10:20].strip()))
                tmp_wss.append(float(line[21:31].strip()))
                tmp_ref.append(float(line[32:42].strip()))
            except Exception as err:
                print(err)
        rss.append(tmp_rss)
        wss.append(tmp_wss)
        ref.append(tmp_ref)
print(len(rss))
print(len(wss))
count_file=-1
for item in os.listdir("./"):
    if str(item)=="SF-1.csv":
        count_file+=1
        f = open(item,'r')
        res = "dbname,seqno,query,exec_time,perf_dev,dev_pcnt,perf_stts,rss,avgrss,vsz,memory,llc_hit,llc_hitm,llc_miss,llc_lookup_stat,llc_hitm_stat,llc_hit_stat,llc_miss_stat,maxrss,avgrss,maxwss,avgrss,ref,maxrss_s,avgrss_s,maxref_s,avgref_s\n"
        lines = f.readlines()
        count=-1
        for line in lines:
            count+=1
            if 0<count<=22:
                index =(count_file*22+count-1)
                res+=line.strip()+","+str(max(rss[index]))+","+str(mean(rss[index]))+","+str(max(ref[index]))+","+str(mean(ref[index]))+"\n"
        print(res)
        f = open(item,'w')

        f.write(res)
        