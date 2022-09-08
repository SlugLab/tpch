#!/bin/bash
for i in {1..22}; do
	echo -n $i '  ';
	awk -f HITMRate.awk SF1-$i-c2c.txt; 
done
