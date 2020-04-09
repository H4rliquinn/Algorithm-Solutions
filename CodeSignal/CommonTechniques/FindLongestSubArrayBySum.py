def findLongestSubarrayBySum(s, arr):
    cache={}
    max_len=0
    sum=0
    res=None
    for x in range(len(arr)):
        sum+=arr[x]
        if sum not in cache:
            cache[sum]=x

        if sum==s:
            max_len=x+1
            res=(0,x)
        elif sum-s in cache:
            if max_len<x-cache[sum-s]+1:
                max_len=x-cache[sum-s]+1
                res=(cache[sum-s]+1,x)
        
    if res:
        return [res[0]+1,res[1]+1]
    else:
        return [-1]
