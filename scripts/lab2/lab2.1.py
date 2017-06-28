#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import os

catal = format (sys.argv[1])
lett = format (sys.argv[2])

dir_list = []
for dirpath, dirnames, filenames in os.walk(catal):
    for f in filenames:
	if f.startswith(lett):
	   fp = os.path.join(dirpath, f)
	   dir_list.append(fp)
	   
print "sorted:"
date_list = [[x, os.path.getctime(x)] for x in dir_list] 
sort_date_list = sorted(date_list, key=lambda x: x[1], reverse=True)
for i in range(len(sort_date_list)):
	print sort_date_list[i][0]
	print sort_date_list[i][1]
	
os.chdir(catal)
filename = raw_input("Enter filename:")
gogo = open (filename,"w+")
for i in range(len(sort_date_list)):
	s2 = str(sort_date_list[i][1])+"\n"
	s0 = "   "
	s1 = str(sort_date_list[i][0])
	gogo.write(s1+s2)				
gogo.close()
   
	   
           


	

