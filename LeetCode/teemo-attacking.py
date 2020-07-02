'''In LOL world, there is a hero called Teemo and his attacking can make his enemy Ashe be in poisoned condition. Now, given the Teemo's attacking ascending time series towards Ashe and the poisoning time duration per Teemo's attacking, you need to output the total time that Ashe is in poisoned condition.
You may assume that Teemo attacks at the very beginning of a specific time point, and makes Ashe be in poisoned condition immediately.

Example 1:
Input: [1,4], 2
Output: 4
Explanation: At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned immediately. 
This poisoned status will last 2 seconds until the end of time point 2. 
And at time point 4, Teemo attacks Ashe again, and causes Ashe to be in poisoned status for another 2 seconds. 
So you finally need to output 4.
 
Example 2:
Input: [1,2], 2
Output: 3
Explanation: At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned. 
This poisoned status will last 2 seconds until the end of time point 2. 
However, at the beginning of time point 2, Teemo attacks Ashe again who is already in poisoned status. 
Since the poisoned status won't add up together, though the second poisoning attack will still work at time point 2, it will stop at the end of time point 3. 
So you finally need to output 3.

Note:
You may assume the length of given time series array won't exceed 10000.
You may assume the numbers in the Teemo's attacking time series and his poisoning time duration per attacking are non-negative integers, which won't exceed 10,000,000.
'''
# import queue
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        # curr=0
        poison_start=0
        poison_end=0
        time=0
        # q=queue.Queue(maxspace=10000)
        
        if len(timeSeries)<1 or duration<1:
            return 0
        
        for x in timeSeries:
            
            #Set up the current range add time
            if poison_start==0:
                poison_start=x
                poison_end=x+duration
                time+=duration
            elif x>poison_end:
                poison_start=x
                poison_end=x+duration
                time+=duration
            elif x>poison_start:
                print("Within",x+duration,poison_end)
                time+=(x+duration)-(poison_end)
                poison_end=x+duration
            print(time)
        return time
