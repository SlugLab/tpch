import os
for i in ["SF-1","SF-10","SF-30","SF-100"]:
    for j in range(1,22):
        print("../run_with_memory_monitor.sh 100 mclient -tperformance -fraw -d "+i+" "+"{:0>2d}".format(j)+".sql")
        os.system("../run_with_memory_monitor.sh 100 mclient -tperformance -fraw -d "+i+" "+"{:0>2d}".format(j)+".sql")