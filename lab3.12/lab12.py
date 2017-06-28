#!/usr/bin/python
import threading
import sys
import random

n = int(format(sys.argv[1]))
tickets = []
money=1000
for i in range(9):
  tickets.append(money)


def trans_1(i,j,summ,event_for_wait, event_for_set):
  global tickets
  if tickets[i]-summ>0:
     event_for_wait.clear() # clean event for future
     while tickets[i]-summ>=0:
       tickets[i]-=summ
       tickets[j]+=summ
       print(tickets[i])
       print(tickets[j])
       print(tickets) 
       if tickets[i]-summ<0:
          print("waiting")
          #event_for_set.set() # set event for neighbor thread
          event_for_wait.wait() # wait for event
          

def func(n):
  for i in range(0,n):
     tick_1 = random.randrange(0,9)
     tick_2 = random.randrange(0,9)
     print("proc "+str(i)+" : "+str(tick_1))
     print("proc "+str(i)+" : "+str(tick_2))
     e1 = threading.Event()
     e2 = threading.Event()
     # init threads
     t1 = threading.Thread(target=trans_1, args=(tick_1,tick_2,300,e1, e2))
     t2 = threading.Thread(target=trans_1, args=(tick_1,tick_2,300,e2, e1))
     # start threads
     t1.start()
     t2.start()
     e1.set() # initiate the first event
     # join threads to the main thread
     t1.join()
     t2.join()

func(n)
print(tickets)
