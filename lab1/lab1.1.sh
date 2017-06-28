#!/bin/bash
catalog=$1
lett=$2
echo "you entered catalog: $catalog";
echo "you entered: $lett";
finded=$(find $catalog -type f -name "$lett*");
echo "$finded"
echo "Enter filename:";
read filename
echo "you entered: $filename";
cd $catalog;
touch "$filename";
for i in $finded;
  do
	du -b "$i";
	j=$(du -b "$i");
	echo "$j">>"$filename";
done
sorted=$(sort "$filename" | sort -n);
cp /dev/null "$filename";
echo "$sorted">>"$filename";

