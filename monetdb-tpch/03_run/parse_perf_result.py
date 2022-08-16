import os
import re

load_lookup=[]
load_miss=[]
load_modified=[]
load_sstate=[]

for item in os.listdir("./"):
    if str(item).endswith("txt"):
        f= open(item,'r')
        lines = f.readlines()
        for line in lines:
            if line.startswith("  Load LLC hit                      :"):
                load_lookup.append(int(line[40:].strip()))
            if line.startswith("  Load Local HITM                   : "):
                load_modified.append(int(line[40:].strip()))
            if line.startswith("  Load MESI State Shared            :"):
                load_sstate.append(int(line[40:].strip()))
            if line.startswith("  Load LLC Misses                   :"):
                load_miss.append((int(line[40:].strip())))

print(len(load_lookup))
print(len(load_miss))
for item in os.listdir("./"):
    if str(item) .endswith("0.csv") or str(item) .endswith("1.csv"):
        f = open(item,'w')
        