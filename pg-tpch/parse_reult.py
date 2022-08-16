
import os

load_lookup=[]
load_miss=[]
load_hitm=[]
load_remote_hitm=[]

for item in os.listdir("/home/psafayen/Postgres/results"):
    if str(item).endswith("txt"):
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
for count_file in range(0,2):
    f = open(item,'r')
    res = "llc_hit,llc_hitm,llc_miss\n"
    lines = f.readlines()
    count=-1
    for line in lines:
        count+=1
        if 0<count<=21:
            index =(count_file*21+count)%84
            print(count_file,count)
            res+=","+str(load_lookup[index])+","+str(load_hitm[index]+load_remote_hitm[index])+","+str(load_miss[index])+"\n"
    print(res)
    f = open(item,'w')

    f.write(res)
    