#!/bin/python3

import math
import os
import random
import re
import sys

"""
Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography. During his last hike he took exactly  steps. For every step he took, he noted if it was an uphill, , or a downhill,  step. Gary's hikes start and end at sea level and each step up or down represents a  unit change in altitude. We define the following terms:

A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked through.

For example, if Gary's path is , he first enters a valley  units deep. Then he climbs out an up onto a mountain  units high. Finally, he returns to sea level and ends his hike.
"""

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
