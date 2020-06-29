'''
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
'''

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        dist=[0]*len(T)


        curr=len(T)-2
        lookup=curr+1
        days=1
        count=0
        #iterate backward through temp list
        while curr>-1:
            #if temp lower add 1 to dist
            if T[curr]<T[lookup]:
                print("Lower")
                dist[curr]=days
                days=1
                curr-=1
                lookup=curr+1
            #if higher loop through dist to find next higher value
            if T[curr]>T[lookup]:
                #add current value to sum
                if dist[lookup]!=0:
                    print("GT",dist,days,lookup)
                    days+=dist[lookup]
                    lookup+=dist[lookup]
                else:
                    print("NF",curr,days)
                    dist[curr]=0
                    days=1
                    curr-=1
                    lookup=curr+1
            count+=1
            if count>50:
                return [-1]
        #return distances
        return dist