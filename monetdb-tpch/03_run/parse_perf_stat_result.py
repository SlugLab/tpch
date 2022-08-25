import os

load_lookup=[]
load_miss=[]
load_hitm=[]
load_hit=[]

for item in sorted(os.listdir("./")):
    if str(item).endswith("txt"):
        f= open(item,'r')
        lines = f.readlines()
        for line in lines:
            if "mem_load_uops_l3_hit_retired.xsnp_none" in line:
                load_lookup.append(int(line[:23].strip().replace(",","")))
            if "mem_load_uops_l3_hit_retired.xsnp_hitm" in line:
                load_hitm.append(int(line[:23].strip().replace(",","")))
            if "mem_load_uops_l3_hit_retired.xsnp_hit" in line:
                load_hit.append(int(line[:23].strip().replace(",","")))
            if "mem_load_uops_l3_hit_retired.xsnp_miss" in line:
                load_miss.append((int(line[:23].strip().replace(",",""))))


count_file=-1
for item in os.listdir("./"):
    if (str(item).endswith("0.csv") or str(item).endswith("1.csv")):
        count_file+=1
        f = open(item,'r')
        res = "dbname,seqno,query,exec_time,perf_dev,dev_pcnt,perf_stts,rss,avgrss,vsz,memory,llc_hit,llc_hitm,llc_miss,llc_lookup_stat,llc_hitm_stat,llc_hit_stat,llc_miss_stat\n"
        lines = f.readlines()
        count=-1
        for line in lines:
            count+=1
            if 0<count<=22:
                index =(count_file*22+count-1)
                res+=line.strip()+","+str(load_lookup[index])+","+str(load_hitm[index]+load_hit[index])+","+str(load_miss[index])+","+ str(load_miss[index])+"\n"
        print(res)
        f = open(item,'w')

        f.write(res)
        