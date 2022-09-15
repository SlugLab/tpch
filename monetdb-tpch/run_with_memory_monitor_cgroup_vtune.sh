#!/bin/bash
first_arg="$1"
shift
echo First argument: "$first_arg"
echo Remaining arguments: "$@"
# set -m

taskset -c 0-7 mserver5 --dbpath=/home/victoryang00/bak/$5/$5 --set monet_vault_key=/home/victoryang00/bak/$5/$5/.vaultkey &
pid1=$!
sudo -u root sh -c "echo $pid1 > /sys/fs/cgroup/memory/my_cgroup/cgroup.procs"
sudo -u root sh -c "echo $(($first_arg * 1024 * 1024 * 1024)) > /sys/fs/cgroup/memory/my_cgroup/memory.limit_in_bytes"

sleep 1
/opt/intel/oneapi/vtune/latest/bin64/vtune -collect uarch-exploration -target-pid $pid1 -r $6-$first_arg-uarch &
pid2=$!
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
        if ! ps -p $pid >/dev/null; then
            if [[ $count == 1 ]]; then
                sleep 0.5
                ps -aux | grep mserver5 | grep -v grep | awk '{print $2}' | xargs kill -INT 

                #    rm /home/victoryang00/bak/SF-100/SF-100/.gdk_lock
                # ps -aux | grep ucevent.py | grep -v grep | awk '{print $2}' | xargs kill -15
                # sleep 0.5
                # ps -aux | grep ucevent.py | grep -v grep | awk '{print $2}' | xargs kill -15
                echo  kill -INT $pid2
                kill -INT $pid2
                rm -rf /home/victoryang00/bak/*/*/.gdk_lock
                # sleep 20
                # perf report -NN -c pid,iaddr --full-symbols --stdio \
                exit 0
            fi
            break
        fi
    done
done
