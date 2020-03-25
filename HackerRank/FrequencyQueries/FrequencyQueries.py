"""
You are given  queries. Each query is of the form two integers described below:
-1,x  : Insert x in your data structure.
-2,y  : Delete one occurence of y from your data structure, if present.
-3,z  : Check if any integer is present whose frequency is exactly . If yes, print 1 else 0.

The queries are given in the form of a 2-D array  of size  where  contains the operation, and  contains the data element.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    # Output array
    output=[]
    # Data from the queries
    data={}
    # the values in this second dict will be the frequency of the frequencies
    frequency={}
    
    # Check for queries
    # if len(queries)<1:
    #     return output
    # for loop through all the queries
    for q in queries:
        # checks for each query type 
        if q[0] == 1:
            if q[1] in data:
                old_f=data[q[1]]
                # increment the data if it exists in the first dict
                data[q[1]]+=1
            else:
                old_f=0
                # init the data to a freq of 1 if it doesn't exist in the first dict
                data[q[1]]=1
            new_f=data[q[1]]
            
            if old_f in frequency and frequency[old_f]>0:
                # decrement the value of the old freq in the second dict
                frequency[old_f]-=1

            if new_f in frequency:
                # increment the value of the new freq in the second dict if it exists 
                frequency[new_f]+=1
            else:
                # init the freq in the second dict to 1 if it doesn't
                frequency[new_f]=1

        if q[0] == 2:
            if q[1] in data and data[q[1]]>0: 
                # decrement the value of the old freq in the second dict
                frequency[data[q[1]]]-=1
                # decrement the data if it exists in the dict
                data[q[1]]-=1
                # increment the value of the new freq in the second dict
                if data[q[1]] in frequency:
                    frequency[data[q[1]]]+=1
                else:
                    frequency[data[q[1]]]=1
            # do nothing if the data isn't in the dict
        if q[0] == 3:
            # check if the second dict has query[1] as a key and if its value > 0
            if q[1] in frequency and frequency[q[1]]>0:
                # add a 1 to our output array
                output.append(1)
            else:
                # add a 0 to our output array
                output.append(0)
    # return our output array
    print(output)
    return output

if __name__ == '__main__':
    f = open('data2.txt', 'r')
    queries = []
    q = f.read().split()
    for x in range(0,len(q),2):
        first=int(q[x])
        second=int(q[x+1])
        queries.append([first,second])
        # print(queries)
    ans = freqQuery(queries)
    numprnt=86
    # print(ans[:numprnt])

    f.close()
    f = open('answer2.txt', 'r')   
    right = f.read().split()
    right=list(map(int,right))
    print(ans,ans==right)