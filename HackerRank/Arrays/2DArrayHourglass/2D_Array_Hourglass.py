"""
Given a  2D Array, :

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:

a b c
  d
e f g
There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

For example, given the 2D array:

-9 -9 -9  1 1 1 
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0
We calculate the following  hourglass values:

-63, -34, -9, 12, 
-10, 0, 28, 23, 
-27, -11, -2, 10, 
9, 17, 25, 18
Our highest hourglass value is  from the hourglass:

0 4 3
  1
8 6 6
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_hourglass=float("-inf")
    for y in range(len(arr)-2):
        for x in range(len(arr[y])-2):
            current_total=0
            current_total+=sum(arr[y][x:x+3])
            current_total+=arr[y+1][x+1]
            current_total+=sum(arr[y+2][x:x+3])
            if current_total>max_hourglass:
                max_hourglass=current_total
    return max_hourglass

if __name__ == '__main__':
    arr=['1 1 1 0 0 0',
        '0 1 0 0 0 0',
        '1 1 1 0 0 0',
        '0 0 2 4 4 0',
        '0 0 0 2 0 0',
        '0 0 1 2 4 0',]
    result = hourglassSum(arr)
    print(result)
