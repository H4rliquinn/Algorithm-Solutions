"""
Emma is playing a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus  or . She must avoid the thunderheads. Determine the minimum number of jumps it will take Emma to jump from her starting postion to the last cloud. It is always possible to win the game.

For each game, Emma will get an array of clouds numbered  if they are safe or  if they must be avoided. For example,  indexed from . The number on each cloud is its index in the list so she must avoid the clouds at indexes  and . She could follow the following two paths:  or . The first path takes  jumps while the second takes .
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    curr=0
    jumps=0
    while curr<len(c)-3:
        if c[curr+2]==0:
            jumps+=1
            curr+=2
        elif c[curr+1]==0:
            jumps+=1
            curr+=1
    jumps+=1

    return jumps



if __name__ == '__main__':
    n=6
    s='000010'
    result = jumpingOnClouds(c)
    print(result)
