import os
for i in range(34,65): # 2GB in node0, 6GB in node1
    os.system("chmem -b -v -d "+str(i))
for i in range(1,33): # 2GB in node0, 6GB in node1
    os.system("chmem -b -v -d "+str(i))
