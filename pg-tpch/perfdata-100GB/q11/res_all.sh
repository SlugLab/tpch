
#!/bin/bash
for i in $(seq 1 6); do
	echo $i;
	awk -f res.awk $1-$i-2-uarch.txt; 
done
