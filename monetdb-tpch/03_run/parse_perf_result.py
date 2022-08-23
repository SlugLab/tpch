import os

load_lookup=[]
load_miss=[]
load_hitm=[]
load_remote_hitm=[]

for item in sorted(os.listdir("./")):
    if str(item).endswith("txt"):
        print (item)
        f= open(item,'r')
        lines = f.readlines()
        for line in lines:
            if line.startswith("  Load LLC hit                      :"):
                load_lookup.append(int(line[40:].strip()))
            if line.startswith("  Load Local HITM                   :"):
                load_hitm.append(int(line[40:].strip()))
            if line.startswith("  Load Remote HITM                  :"):
                load_remote_hitm.append(int(line[40:].strip()))
            if line.startswith("  Load LLC Misses                   :"):
                load_miss.append((int(line[40:].strip())))

print(len(load_lookup))
print(len(load_miss))
count_file=-1
for item in os.listdir("./"):
    if (str(item).endswith("0.csv") or str(item).endswith("1.csv")):
        count_file+=1
        f = open(item,'r')
        res = "dbname,seqno,query,exec_time,perf_dev,dev_pcnt,perf_stts,rss,avgrss,vsz,memory,llc_hit,llc_hitm,llc_miss\n"
        lines = f.readlines()
        count=-1
        for line in lines:
            count+=1
            if 0<count<=22:
                index =(count_file*22+count-1)
                res+=line.strip()+","+str(load_lookup[index])+","+str(load_hitm[index]+load_remote_hitm[index])+","+str(load_miss[index])+"\n"
        print(res)
        f = open(item,'w')

        f.write(res)
        