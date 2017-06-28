#!/bin/bash
catalog1=$1
catalog2=$2
if [ $catalog1 = $catalog2 ]
then
	exit 0;
fi
echo "Enter word:";
read lett
echo "you entered: $lett";
finded=$(find $catalog1 -type f -name "$lett*");
typeset -i count filesize;
let count=0 filesize=0;
for i in $finded;
  do
	du -b "$i";
	let count++;
	let filesize=$(du -b "$i" | head -n1 | awk '{print $1}')+filesize;
	cp $i $catalog2;
done
echo "$count files have been copyed"
echo "total size of files = $filesize bytes"
