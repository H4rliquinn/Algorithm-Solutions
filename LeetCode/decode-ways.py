'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        list(s)
        if s[0]=='0':
            return 0
        count=[0]*len(s)
        count[0]=1
        
        for x in range(1,len(s)):
            curr=int(s[x])
            prev=int(s[x-1:x+1])
            if curr>=1 and curr<=9:
                count[x]+=count[x-1]
            if prev>=10 and prev<=26:
                if x>=2:
                    count[x]+=count[x-2]
                else:
                    count[x]+=1      
        return count[-1]
