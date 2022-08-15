#!/bin/bash
first_arg="$1"
shift
echo First argument: "$first_arg"
echo Remaining arguments: "$@"
# set -m
mserver5 --dbpath=/home/victoryang00/tpch-scripts/monetdb-tpch/$5/$5 --set monet_vault_key=/home/victoryang00/tpch-scripts/monetdb-tpch/$5/$5/.vaultkey &
echo mserver5 --dbpath=/home/victoryang00/tpch-scripts/monetdb-tpch/$5/$5 --set monet_vault_key=/home/victoryang00/tpch-scripts/monetdb-tpch/$5/$5/.vaultkey 
pid1=$!
# echo $pid1 > /sys/fs/cgroup/memory/my_cgroup/cgroup.procs
# echo $(($first_arg * 1024 * 1024 * 1024)) > /sys/fs/cgroup/memory/my_cgroup/memory.limit_in_bytes
#../run_with_memory_monitor.sh',str(args.memory), "mclient", '-tperformance', '-fraw', '-d', db, queryfile
sleep 2 
# python3 /home/victoryang00/pmu-tools/ucevent/ucevent.py --interval 100 -o $5-$6.csv --csv out.csv -x , CBO.LLC_VICTIMS.M_STATE CBO.LLC_VICTIMS.MISS CBO.LLC_VICTIMS  &
perf c2c record -F 60000 -a sleep 1000 &
pid2=$!
"$@" &
pid=$!
# echo $pid > /sys/fs/cgroup/memory/my_cgroup/cgroup.procs
# echo $(($first_arg * 1024 * 1024 * 1024)) > /sys/fs/cgroup/memory/my_cgroup/memory.limit_in_bytes
while true; do
    line=$(ps auxh -q $pid1)
    if [ "$line" == "" ]; then
        break;
    fi
    echo $line >> log.out
    for child in $(pgrep -P $pid1);
    do
      line=$(ps auxh -q $child)
      if [ "$line" == "" ]; then
          continue;
      fi
      echo $line >> log.out
    done
    sleep 0.005
if ! ps -p $pid > /dev/null
then
sleep 0.5
   ps -aux | grep mserver5| grep -v grep | awk '{print $2}' | xargs kill -9
   #    rm /home/victoryang00/tpch-scripts/monetdb-tpch/SF-100/SF-100/.gdk_lock
    # ps -aux | grep ucevent.py | grep -v grep | awk '{print $2}' | xargs kill -15 
# sleep 0.5

    # ps -aux | grep ucevent.py | grep -v grep | awk '{print $2}' | xargs kill -15 
   kill -INT $pid2

   sleep 2
   perf c2c report -NN -c pid,iaddr --full-symbols --stdio > $5-$6-c2c.txt
fi
done
awk 'BEGIN { maxvsz=0; maxrss=0; count=0; sum=0; sum1=0;} \
    { if ($5>maxvsz) {maxvsz=$5}; if ($6>maxrss) {maxrss=$6};  sum=sum+$6; count=count+1; sum1=sum1+$5;}\
    END { print "vsz=" maxvsz " rss=" maxrss " avgrss=" sum/count;}' log.out
rm log.out
exit 0

