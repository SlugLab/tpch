
#!/bin/bash
for i in $(seq 1 6); do
	echo $i;
	awk -f res.awk q$1/$1-$i-uarch.txt; 
done
