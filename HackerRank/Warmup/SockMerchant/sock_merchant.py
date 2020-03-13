#!/bin/python3

import math
import os
import random
import re
import sys

"""
John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are  socks with colors . There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .
"""

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    drawer={}
    for sock in ar:
        if drawer.get(sock,None):
            drawer[sock]+=1
        else:
            drawer[sock]=1
    total=0
    for val in drawer.values():
        total+=val//2
    return total


if __name__ == '__main__':
    n = 9
    ar = [10, 20, 20 ,10, 10, 30,50 ,10 ,20]
    result = sockMerchant(n, ar)
    print(result)
