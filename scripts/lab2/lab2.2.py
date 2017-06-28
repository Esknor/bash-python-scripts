#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import os

catal = format (sys.argv[1])
dir_list = []

for dirpath, dirnames, filenames in os.walk(catal):
	for d in dirnames:
		 dp = os.path.join(dirpath, d)
	   	 dir_list.append(dp)

def f1(path):
	total_size = 0
	dir_list = [os.path.join(path, x) for x in os.listdir(path)]
        if dir_list:
    		date_list = [[x, os.path.getsize(x)] for x in dir_list] 
    		for i in range(len(dir_list)):
			total_size += os.path.getsize(dir_list[i])
	return total_size


date_list = [[dir_list[i], f1(dir_list[i])] for i in range(len(dir_list))] 
sort_date_list = sorted(date_list, key=lambda i: i[1], reverse=True)        
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
	gogo.write(s1+s0+s2)				
gogo.close()








