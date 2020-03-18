"""
You have an array of integers nums and an array queries, where queries[i] is a pair of indices (0-based). Find the sum of the elements in nums from the indices at queries[i][0] to queries[i][1] (inclusive) for each query, then add all of the sums for all the queries together. Return that number modulo 109 + 7.
"""
def sumInRange(nums, queries):
    #Preprocessed nums to speed sum
    #This is brilliant
    
    cache=nums[:]
    total=0
    
    for i in range(1, len(cache)): 
        cache[i] = cache[i] + cache[i-1] 

    for query in queries:
        if query[0]==0:
            start=0
        else:
            start=cache[query[0]-1]
        total+=(cache[query[1]]-start)

    return total%1000000007

    # Too Slow
    # cache={}
    # total=0
    # print(len(nums),len(queries))
    # for query in queries:
    #     adds=0
    #     if cache.get((query[0],query[1]),None):
    #         adds=cache[(query[0],query[1])]
    #     else:
    #         adds=sum(nums[query[0]:query[1]+1])
    #         cache[(query[0],query[1])]=adds
    #     total+=adds
    # return total%1000000007

    #Still Slow
    # values={}
    # total=0
    # for query in queries:
    #     for x in range(query[0],query[1]+1):
    #         if values.get(x,None):
    #             values[x]+=1
    #         else:
    #             values[x]=1
    # for key in values.keys():
    #     total+=nums[key]*values[key]
    # return total%1000000007