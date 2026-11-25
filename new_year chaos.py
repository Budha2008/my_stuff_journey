"""

q=[1,9,3,5,4,8,7]
count=0
l=[]
for i in range(len(q)-1):
    if q[i]>q[i+1]:
        print("error occured at",q[i])
        t=q[i+1]
        q[i+1]=q[i]
        q[i]=t
        count=count+1
        print("count",count)
        
        print(q)

"""



import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
 count=0
 bribe=0
 l=[]
 counts=[]
 for h in range(len(q)): 
   for i in range(len(q)-1):
        
        if q[i]>q[i+1]:
            l.append(q[i])
            t=q[i+1]
            q[i+1]=q[i]   #we are swaping if first is larger
            q[i]=t
            bribe=bribe+1
            print("it is bribe",bribe)
            print(q)
            print(i)
            print(l)

 for i in range(len(l)):
     counts.append(l.count(l[i]))
 print(counts)
 for  i in counts:
     if i>=3:
         count=1
         print("Too chaotic")
         break
 if count==0:
     print(bribe)
     
 #if count>=3:
    #print("Too chaotic")
 #else:

    #print(q)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)







