#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes=0
    for x in range(len(q)-1,-1,-1):
        if q[x-1]==x+1 and len(q)>1:
            q[x],q[x-1]=q[x-1],q[x]
            bribes+=1
        elif q[x-2]==x+1 and len(q)>1:
            q[x],q[x-1],q[x-2]=q[x-2],q[x],q[x-1]
            bribes+=2
        elif q[x]!=x+1:
            print("Too chaotic")
            return "Too chaotic"
    print(bribes)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
