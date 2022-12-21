#!/bin/bash
SF="SF-100"
for i in $(seq 7 7); do
    echo "Running query: $i"
    ii=$(printf "%02d" $i)

    taskset -c 8-15 mserver5 --dbpath=/scratchNVME/bak/$SF/$SF --set monet_vault_key=/scratchNVME/bak/$SF/$SF/.vaultkey &
    # numactl --membind=0 --cpubind=1  mserver5 --dbpath=/scratchNVME/bak/$SF/$SF --set monet_vault_key=/scratchNVME/bak/$SF/$SF/.vaultkey &
    pidS=$!
    echo "Server Pid:" $pidS

    sleep 5
    count=0
    while true; do
        sleep 2
        index=$(($count + 1))
        out_base=q$i-$SF-${index}-L30p-numa

        /usr/bin/time -o "results/$out_base.time" -f "%e"  mclient -tperformance -fraw -d $SF 03_run/$ii.sql > "results/$out_base.txt" &
        pid=$!
        echo "Client" $count "Pid:" $pid

        count=$(($count + 1))
        log_dir="results/$out_base.mem"
        echo "" > $log_dir
       
        while true; do

	    numastat -m >> "results/$out_base.system-numstat"
	    
            ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem  |head -n 2 |tail -n 1 |awk '{print $1}' | xargs numastat -p >> "results/$out_base.numastat"
            pids=`pstree -p $pidS | grep -o '([0-9]\+)' | grep -o '[0-9]\+'`
            for child in $pids; do
                line=$(ps auxh -q $child)
                if [ "$line" == "" ]; then
                    continue
                fi
                echo $line >>$log_dir

            done

	    
            sleep 0.005
            if ! ps -p $pid >/dev/null; then
                break
            fi
            done 
            if [[ $count == 5 ]]; then
                sleep 0.5
                for j in $(seq 1 $count); do
                    out_base=q$i-$SF-$j-L30p-numa
                    log_dir="results/$out_base.mem"
                    awk 'BEGIN { maxvsz=0; maxrss=0; count=0; sum=0; sum1=0; } \
                        { if ($5>maxvsz) {maxvsz=$5}; if ($6>maxrss) {maxrss=$6}; sum=sum+$6; count=count+1; sum1=sum1+$5; }\
                        END { print maxvsz "," sum1/count "," maxrss "," sum/count; }' $log_dir > "results/$out_base.mem_summary"
                done
                ps -aux | grep mserver5 | grep -v grep | awk '{print $2}' | xargs kill -INT
                rm -rf /scratchNVME/bak/*/*/.gdk_lock
                break
            fi
        done
done
ps -aux | grep mserver5 | grep -v grep | awk '{print $2}' | xargs kill -INT
rm -rf /home/scratchNVME/bak/*/*/.gdk_lock
