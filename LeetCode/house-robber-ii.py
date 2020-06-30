'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0
        if len(nums) == 1: 
            return nums[0] 
        if len(nums) == 2: 
            return max(nums[0],nums[1])
        
        def robber_helper(nums,i,j):
            if i==j:
                return nums[i]
            cache = [0]*len(nums)      
            cache[i]=nums[i]
            cache[i+1]=max(nums[i+1],cache[i])
            
            for x in range(i+2, j): 
                cache[x] = max(nums[x]+cache[x-2], cache[x-1])
            return cache[j-1]
        
        max1=robber_helper(nums,0,len(nums)-1)
        max2=robber_helper(nums,1,len(nums))
         
        return max(max1,max2)
