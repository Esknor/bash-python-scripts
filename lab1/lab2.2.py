#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import os
import shutil

catal1 = format (sys.argv[1])
catal2 = format (sys.argv[2])

if catal1==catal2:
	print("this is a same catalog!")
	sys.exit()

lett = raw_input("word:")

counter_files=0
counter_sizes=0
for dirpath, dirnames, filenames in os.walk(catal1):
    for f in filenames:
	if f.startswith(lett):
	   fp = os.path.join(dirpath, f)
	   shutil.copy2(fp,catal2)
	   counter_files+=1
	   counter_sizes+=os.path.getsize(fp)
           print(f,os.path.getsize(fp))

print("total size: %s byte" % counter_sizes)
print("totaly files: %s" % counter_files)

