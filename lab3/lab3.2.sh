#!/bin/bash
exp1=$(sed -n 's/8-0/0-/p' filetel);
exp2=$(sed -n 's/8-0/0-/p' filetel);
exp3=$(sed -n 's/8-2/0-2/p' filetel);
exp4=$(sed -n 's/8-10/00/p' filetel);
touch "filenamelab2";
echo "$exp1">>"filenamelab2";
echo "$exp2">>"filenamelab2";
echo "$exp3">>"filenamelab2";
echo "$exp4">>"filenamelab2";
