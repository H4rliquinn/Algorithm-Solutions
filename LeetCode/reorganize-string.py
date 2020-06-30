"""
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.
Example 1:
Input: S = "aab"
Output: "aba"

Example 2:
Input: S = "aaab"
Output: ""
"""
class Solution:
    def reorganizeString(self, S: str) -> str:
        rtn=""
        prev_char=""
        first_char=""
        hold=[]
        
        def useHold(first_char,prev_char,rtn):
            if len(hold)>0:
                rep=hold[0]
                if rep!=prev_char:
                    prev_char=hold.pop(0)
                    rtn+=prev_char
                elif rep!=first_char:
                    first_char=hold.pop(0)
                    rtn=first_char+rtn 
            return (first_char,prev_char,rtn)
        
        for x in S:
            if first_char=="":
                first_char=x
                first_char,prev_char,rtn=useHold(first_char,prev_char,rtn)
            if x!=prev_char:
                rtn+=x
                prev_char=x
                first_char,prev_char,rtn=useHold(first_char,prev_char,rtn)
            elif x!=first_char:
                first_char=x
                rtn=x+rtn
            else:
                hold.append(x)
        
        while len(hold)>0:
            cur=hold.pop(0)
            pChar=""
            index=0
            flag=False
            for c in rtn:
                if c!=cur and pChar!=cur:
                    rtn=rtn[0:index]+cur+rtn[index:]
                    flag=True
                    break
                pChar=c
                index+=1 
            if flag==False:
                return ""
        return rtn
