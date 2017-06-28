#!/usr/bin/python
import threading
import sys
import random
import time

n = int(format(sys.argv[1]))
tickets = []
money=1000
for i in range(9):
  tickets.append(money)


def trans_1(num,i,j,summ):
  global tickets
  if tickets[i]-summ>0:
     print("proc "+str(num)+" : "+str(i))
     print("proc "+str(num)+" : "+str(j))
     while tickets[i]-summ>=0:
       tickets[i]-=summ
       tickets[j]+=summ
       print(tickets[i])
       print(tickets[j])
       print(tickets) 
       if tickets[i]-summ<0:
          print("waiting")
          time.sleep(1)
          trans_1(num,i,j,summ)
          

def func(n):
  if(n == 1):
     t0 = threading.Thread(target=trans_1, args=(0,random.randrange(0,9),random.randrange(0,9),300))
     t0.start()
     t0.join() 
     t1 = threading.Thread(target=trans_1, args=(1,random.randrange(0,9),random.randrange(0,9),300))
     t1.start()
     t1.join()
  elif(n == 2):
     t0 = threading.Thread(target=trans_1, args=(0,random.randrange(0,9),random.randrange(0,9),300))
     t0.start()
     t0.join() 
     t1 = threading.Thread(target=trans_1, args=(1,random.randrange(0,9),random.randrange(0,9),300))
     t1.start()
     t1.join()
     t3 = threading.Thread(target=trans_1, args=(2,random.randrange(0,9),random.randrange(0,9),300))
     t3.start()
     t3.join() 
  elif(n == 3):
     t0 = threading.Thread(target=trans_1, args=(0,random.randrange(0,9),random.randrange(0,9),300))
     t0.start()
     t0.join() 
     t1 = threading.Thread(target=trans_1, args=(1,random.randrange(0,9),random.randrange(0,9),300))
     t1.start()
     t1.join()
     t2 = threading.Thread(target=trans_1, args=(2,random.randrange(0,9),random.randrange(0,9),300))
     t2.start()
     t2.join() 
     t3 = threading.Thread(target=trans_1, args=(3,random.randrange(0,9),random.randrange(0,9),300))
     t3.start()
     t3.join()
  elif(n == 4):
     t0 = threading.Thread(target=trans_1, args=(0,random.randrange(0,9),random.randrange(0,9),300))
     t0.start()
     t0.join() 
     t1 = threading.Thread(target=trans_1, args=(1,random.randrange(0,9),random.randrange(0,9),300))
     t1.start()
     t1.join()
     t2 = threading.Thread(target=trans_1, args=(2,random.randrange(0,9),random.randrange(0,9),300))
     t2.start()
     t2.join() 
     t3 = threading.Thread(target=trans_1, args=(3,random.randrange(0,9),random.randrange(0,9),300))
     t3.start()
     t3.join()
     t4 = threading.Thread(target=trans_1, args=(4,random.randrange(0,9),random.randrange(0,9),300))
     t4.start()
     t4.join()
  elif(n == 5):
     t0 = threading.Thread(target=trans_1, args=(0,random.randrange(0,9),random.randrange(0,9),300))
     t0.start()
     t0.join() 
     t1 = threading.Thread(target=trans_1, args=(1,random.randrange(0,9),random.randrange(0,9),300))
     t1.start()
     t1.join()
     t2 = threading.Thread(target=trans_1, args=(2,random.randrange(0,9),random.randrange(0,9),300))
     t2.start()
     t2.join() 
     t3 = threading.Thread(target=trans_1, args=(3,random.randrange(0,9),random.randrange(0,9),300))
     t3.start()
     t3.join()
     t4 = threading.Thread(target=trans_1, args=(4,random.randrange(0,9),random.randrange(0,9),300))
     t4.start()
     t4.join()
     t5 = threading.Thread(target=trans_1, args=(5,random.randrange(0,9),random.randrange(0,9),300))
     t5.start()
     t5.join()


func(n)
print(tickets)
