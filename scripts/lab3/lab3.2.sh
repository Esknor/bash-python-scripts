#!/bin/bash
exp=$(sed 's/#[a-Z0-9]*$//g' ffile);
touch "filenamelab2";
echo "$exp">>"filenamelab2";
sed -i '/^\s*$/d' filenamelab2;

