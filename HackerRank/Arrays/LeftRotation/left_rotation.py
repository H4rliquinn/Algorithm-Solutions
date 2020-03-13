#!/bin/python3
"""
A left rotation operation on an array shifts each of the array's elements  unit to the left. For example, if  left rotations are performed on array , then the array would become .

Given an array  of  integers and a number, , perform  left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.
"""
import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    split=d%len(a)
    return a[split:]+a[:split]

if __name__ == '__main__':
    a='1 2 3 4 5'
    d=4
    result = rotLeft(a, d)
    print(result)



