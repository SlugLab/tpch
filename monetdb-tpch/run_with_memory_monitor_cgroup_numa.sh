#!/bin/bash
first_arg="$1"
shift
echo First argument: "$first_arg"
echo Remaining arguments: "$@"

second_arg="$1"
shift
echo Second argument: "$second_arg"
echo Remaining arguments: "$@"
# set -m

taskset -c 0-7 mserver5 --dbpath=/home/victoryang00/bak/$5/$5 --set monet_vault_key=/home/victoryang00/bak/$5/$5/.vaultkey &

pid1=$!
sudo -u root sh -c "echo $pid1 > /sys/fs/cgroup/memory/numa/cgroup.procs"
sudo -u root sh -c "echo $(($first_arg * 1024 * 1024 * 1024)) > /sys/fs/cgroup/memory/numa/memory.limit_in_bytes"
# sudo -u root sh -c "echo $pid1 > /sys/fs/cgroup/cpuset/numa/cgroup.procs "
# sudo -u root sh -c "echo 0-1 > /sys/fs/cgroup/cpuset/numa/cpuset.mems"
# sudo -u root sh -c "echo $second_arg > /sys/fs/cgroup/cpuset/numa/cpuset.cpus"


# echo $(($second_arg))  /mnt/my_cgroups/cpusets/cpuset.cpus

count=0
### Draw graph!!!!
while true; do
    #../run_with_memory_monitor.sh',str(args.memory), "mclient", '-tperformance', '-fraw', '-d', db, queryfile
    sleep 2
    # python3 /home/victoryang00/pmu-tools/ucevent/ucevent.py --interval 100 -o $5-$6.csv --csv out.csv -x , CBO.LLC_VICTIMS.M_STATE CBO.LLC_VICTIMS.MISS CBO.LLC_VICTIMS  &
    "$@" &
    pid=$!
    count=$(($count + 1))

    while true; do
        sleep 0.005
        numastat -p $pid1 >> $5-$6-numastat-$first_arg-$second_arg.txt
        if ! ps -p $pid >/dev/null; then
            if [[ $count == 1 ]]; then
                sleep 0.5
                ps -aux | grep mserver5 | grep -v grep | awk '{print $2}' | xargs kill -INT 
                ps -aux | grep numastat | grep -v grep | awk '{print $2}' | xargs kill -INT 
                rm -rf /home/victoryang00/bak/*/*/.gdk_lock
                # sleep 20
                # perf report -NN -c pid,iaddr --full-symbols --stdio \
                exit 0
            fi
            break
        fi
    done
done
