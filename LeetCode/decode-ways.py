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
        count=1
        used=1
        
        list(s)
        if s[0]=='0':
            count=0
            used=0
        
        for x in range(len(s)):
            if x>0:
                if int(s[x-1]+s[x])>26:
                    if used==1:
                        used=0
                    else:
                        count+=1
                else:
                    print("NO",x)
                    if used==0:
                        used=1
                        count+=1
                    else:
                        used=1
                        count+=1
        return count
