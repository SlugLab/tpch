import os
import time
for i in ["SF-100"]:
    for j in range(2,13):
        for k in [8,4,2]:
            for ii in range(1,5):
                print("timeout 1h ../run_with_memory_monitor_cgroup_numa.sh "+ str(k)+" 0-" + str(15+2**(5-ii))+" mclient -tperformance -fraw -d "+i+" "+"{:0>2d}".format(j)+".sql")
                exit = os.system("timeout 1h ../run_with_memory_monitor_cgroup_numa.sh "+ str(k)+" 0-" + str(15+2**(5-ii))+" mclient -tperformance -fraw -d "+i+" "+"{:0>2d}".format(j)+".sql")
                print("exit",exit)
                if exit!=0:
                    os.system("ps -aux | grep mserver5 | grep -v grep | awk '{print $2}' | xargs kill -INT")
                    os.system("rm -rf /home/victoryang00/bak/*/*/.gdk_lock")