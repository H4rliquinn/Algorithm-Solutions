"""
You have an array of integers nums and an array queries, where queries[i] is a pair of indices (0-based). Find the sum of the elements in nums from the indices at queries[i][0] to queries[i][1] (inclusive) for each query, then add all of the sums for all the queries together. Return that number modulo 109 + 7.
"""
def sumInRange(nums, queries):
    # Too Slow
    # total=0
    # for query in queries:
    #     sum=0
    #     for x in range(query[0],query[1]+1):
    #         sum+=nums[x]
    #     total+=sum
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