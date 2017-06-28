#!/usr/bin/python
import sys
import threading


def file_lenght():
    f = open('in.sh', 'r')
    l=0
    for line in f:
      l+=1
    return l


l_f = file_lenght()
sys.stdout.write(str(l_f)+"\n")

def writer(l,start,arr):
    file = open('in.sh')
    line = file.readlines()
    for i in range(start,l,2):
        arr.append(line[i])


def sender(l,wstart,sstart,event_for_wait, event_for_set):
    arr = []
    writer(l,wstart,arr)
    for i in range(sstart,len(arr),2):
	if sstart == 1:
           event_for_wait.wait() # wait for event
           event_for_wait.clear() # clean event for future
           sys.stdout.write(arr[i-1])
	   sys.stdout.write(arr[i])
           event_for_set.set() # set event for neighbor thread   
	if sstart == 0:
           event_for_wait.wait() # wait for event
           event_for_wait.clear() # clean event for future
	   sys.stdout.write(arr[i])
	   sys.stdout.write(arr[i+1])
           event_for_set.set() # set event for neighbor thread
        

e1 = threading.Event()
e2 = threading.Event()
t1 = threading.Thread(target=sender, args=(l_f,0,0,e1, e2))
t2 = threading.Thread(target=sender, args=(l_f,1,1,e2, e1))
t1.start()
t2.start()

e1.set() # initiate the first event

# join threads to the main thread
t1.join()
t2.join()
