#!/bin/bash
file10=$(cat file10)
let i=0 count_zero=0 count_one=0;
touch "fil";
for f in $file10:
  do
	let i+=1;
	line_i=$(sed -n $i'p' file10);
	echo "$line_i"
	echo "$line_i">>"fil";
	let count_zero=$(grep -o '0' 'fil' | wc -m)/2;
	let count_one=$(grep -o '1' 'fil' | wc -m)/2;
	echo "1:$count_one";
	echo "0:$count_zero";
	echo "line: $i";
	let res_one=$count_one%2
	let res_zero=$count_zero%3
	if [ $res_one -eq 0 ] && [ $res_zero -eq 0 ]; then
		echo "zashlo";
		touch "filenamelab3.1";
		echo "$line_i">>"filenamelab3.1";
	fi 
	cp /dev/null fil	
  done
sed -i 's/[^0-1]//g' 'filenamelab3.1'
rm fil;	


