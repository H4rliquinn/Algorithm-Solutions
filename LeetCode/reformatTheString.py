class Solution:
    def reformat(self, s: str) -> str:
        # Edge Case
        if len(s)==0:
            return ""
        # Prep string 
        news=list(s)
        
        digits=[]
        alpha=[]
        res=[]
        for x in range(len(news)):
            if news[x].isdigit():
                digits.append(news[x])
            else:
                alpha.append(news[x])
        diff=abs(len(digits)-len(alpha))
        if diff>1:
            return ""
        else:
            if len(digits)>len(alpha):
                for x in range(len(digits)-1):
                    res.append(digits.pop())
                    res.append(alpha.pop())
                res.append(digits.pop())
            elif len(digits)<len(alpha):
                for x in range(len(alpha)-1):
                    res.append(alpha.pop())
                    res.append(digits.pop())
                res.append(alpha.pop())
            else:
                for x in range(len(digits)):
                    res.append(alpha.pop())
                    res.append(digits.pop())
        return "".join(res)