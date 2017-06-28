#!/usr/bin/python
from subprocess import Popen, PIPE
import os
import sys
import subprocess

pipe = Popen("python 3.py",shell=True,stdout=PIPE, stderr=PIPE)

pipe.wait()    
res = pipe.communicate() 
if pipe.returncode:
    print res[1]
print 'result pipe:', res[0]

pipe.stdout.close()
gogo = open ("file.sh","w+")
gogo.write(res[0])
gogo.close()


file = open('file.sh')
gogo = open ("out.sh","w+")
line = file.readlines()
try:
   for i in range(4,int(line[0]),4):
	gogo.write(line[i-3])
	gogo.write(line[i-2])
	gogo.write(line[i-1])
        gogo.write(line[i])

except IndexError:
	gogo.write("end")

file.close()
gogo.close()

