"""
You have been asked to help study the population of birds migrating across the continent. Each type of bird you are interested in will be identified by an integer value. Each time a particular kind of bird is spotted, its id number will be added to your array of sightings. You would like to be able to find out which type of bird is most common given a list of sightings. Your task is to print the type number of that bird and if two or more types of birds are equally common, choose the type with the smallest ID number.

For example, assume your bird sightings are of types . There are two each of types  and , and one sighting of type . Pick the lower of the two types seen twice: type .
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    # Init birds Dict
    birds={1:0,2:0,3:0,4:0,5:0}
    # Tracking Vars
    max_sightings=0
    popular_birds={}

    # Loop through sightings
    for x in arr:
        birds[x]+=1
        # If new max, set max and create new bird nest
        if birds[x]>max_sightings:
            max_sightings=birds[x]
            popular_birds={x}
        # If tie for max, add bird to nest
        elif birds[x]==max_sightings:
            popular_birds.add(x)
    # Return the smallest bird
    return min(popular_birds)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
