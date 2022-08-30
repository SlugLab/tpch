import os
import time
for i in ["SF-10","SF-30","SF-100"]:
    for j in range(1,23):
        print("../run_with_memory_monitor_wss.sh 1 mclient -tperformance -fraw -d "+i+" "+"{:0>2d}".format(j)+".sql")
        os.system("../run_with_memory_monitor_wss.sh 1 mclient -tperformance -fraw -d "+i+" "+"{:0>2d}".format(j)+".sql")