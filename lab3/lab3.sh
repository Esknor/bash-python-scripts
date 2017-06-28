#!/bin/bash
word=$(grep '[0-1][0-1]' fl);
pattern1="$word"'10';
pattern2="$word"'11';
pattern3="$word"'00';
exp=$(awk "!/$pattern1|$pattern2|$pattern3|[a-z]|10$/" file1001);
echo $exp
#touch "filenamelab1";
#echo "$exp">>"filenamelab3";
