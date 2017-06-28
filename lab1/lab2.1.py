#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import os

catal = format (sys.argv[1])
lett = format (sys.argv[2])
arr_sort = []
l=0
for dirpath, dirnames, filenames in os.walk(catal):
    for f in filenames:
	if f.startswith(lett):
	   fp = os.path.join(dirpath, f)
           print(f,os.path.getsize(fp))
	   arr_sort.append(os.path.getsize(fp))
	   arr_sort.append(f)
	   l+=2
if not arr_sort:
	print("nothing finded")
	sys.exit()
temp_s=0
temp_n=""
ext=0
while ext==0:
	ext=1	
	for i in range(0,l-2,2):
		if arr_sort[i]>arr_sort[i+2]:
		   temp_s=arr_sort[i]
		   temp_n=arr_sort[i+1]
		   arr_sort[i]=arr_sort[i+2]
		   arr_sort[i+2]=temp_s
		   arr_sort[i+1]=arr_sort[i+3]
		   arr_sort[i+3]=temp_n
		   ext=0 				    
print(arr_sort)
os.chdir(catal)
filename = raw_input("Enter filename:")
gogo = open (filename,"w+")
for i in range(0,l,1):
	if i%2==0:
		s = str(arr_sort[i])+" byte "
		gogo.write(s)
	else :
		s = str(arr_sort[i])+"\n"
		gogo.write(s)
gogo.close()
