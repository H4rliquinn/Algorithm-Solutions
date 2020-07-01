"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[1]*len(nums)
        r=[1]*len(nums)
        prod=1
        opp_prod=1
        opp_x=len(nums)-1
        for x in range(len(nums)):
            if x!=0:
                prod*=nums[x-1]
                opp_prod*=nums[opp_x-x+1]
            l[x]=prod
            r[opp_x-x]=opp_prod

        return [x*y for x,y in zip(l,r)]