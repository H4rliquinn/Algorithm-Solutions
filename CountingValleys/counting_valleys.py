#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    #Track height
    height=0
    #Count Valleys
    valleys=0

    #Loop through hike
    for step in s:
        #Check for upstep
        if step=='U':
            height+=1
            #Test if sea level
            if height==0:
                #Found a valley!
                valleys+=1
        else:
            height-=1
    return valleys

if __name__ == '__main__':
    n=8
    s='UDDDUDUU'
    result = countingValleys(n, s)
    print(result)
