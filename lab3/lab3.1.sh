#!/bin/bash
word=$(grep '[0-1][0-1]' fl);
pattern1="$word"'10';
pattern2="$word"'11';
pattern3="$word"'00';
#grep '[0-1]*[1][0]*[0][1]*[0-1]' | egrep -v '[0-1]*1010*[0-1]|[[:alpha:]]' file1001
exp=$(egrep -v "$pattern1|[[:alpha:]]|$pattern2|$pattern3|10$" file1001);
echo $exp;
#touch "filenamelab1";
#echo "$exp">>"filenamelab1";

