'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''
def removeDuplicates(self, nums: List[int]) -> int:
    current_value=nums[0]
    x=1
    while x<len(nums):
        # print(x,nums,current_value)
        if nums[x]==current_value:
            nums.pop(x)
        else:
            current_value=nums[x]
            x+=1
    # print(x,nums,current_value)
    return len(nums)
