#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps=0
    for x in range(len(arr)):
        #Too Slow
        # if arr[x]!=x+1:
        #     loc=arr.index(x+1)
        #     arr[x],arr[loc]=arr[loc],arr[x]
        #     swaps+=1
        while arr[x]!=x+1:
            arr[arr[x]-1],arr[x]=arr[x],arr[arr[x]-1]
            swaps+=1
    print(swaps)
    return swaps

if __name__ == '__main__':
    

    

    arr =[1,3,5,2,4,6,7]

    res = minimumSwaps(arr)
    print(res)
