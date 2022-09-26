import os
import time
for i in ["SF-100"]:
    for j in range(1, 23):
        for k in [12, 10, 8, 6]:
            print("timeout 1h ../run_with_memory_monitor_cgroup_numa.sh " + str(k) +
                  " " + str((k-4)/4)+" mclient -tperformance -fraw -d "+i+" "+"{:0>2d}".format(j)+".sql")
            exit = os.system("timeout 1h ../run_with_memory_monitor_cgroup_numa.sh " + str(
                k)+" " + str((k-4)/4)+" mclient -tperformance -fraw -d "+i+" "+"{:0>2d}".format(j)+".sql")
            print("exit", exit)
            if exit != 0:
                os.system(
                    "ps -aux | grep mserver5 | grep -v grep | awk '{print $2}' | xargs kill -INT")
                os.system("rm -rf /home/victoryang00/bak/*/*/.gdk_lock")
