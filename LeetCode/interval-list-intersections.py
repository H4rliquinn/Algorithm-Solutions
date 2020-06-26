'''Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
Return the intersection of these two interval lists.
(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
'''

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        def calculate_interval(A,B):
            LL=A[0]
            LH=A[1]
            HL=B[0]
            HH=B[1]
            
            if max(LL,HL)>min(LH,HH):
             return []
            return [max(LL,HL),min(LH,HH)]
            # print(A,B)
        
        rslt=[]
        if len(A)>0 and len(B)>0:
            x=0
            y=0
            temp=calculate_interval(A[x],B[y])
            if len(temp)>0:
                rslt.append(temp)
            
            while x<len(A)-1:
                x+=1
                temp=calculate_interval(A[x],B[y])
                if len(temp)>0:
                    rslt.append(temp)
                if y<len(B)-1:
                    y+=1
                    temp=calculate_interval(A[x],B[y])
                    if len(temp)>0:  
                        rslt.append(temp)   
            if y<len(B)-1:
                y+=1
                temp=calculate_interval(A[x],B[y])
                if len(temp)>0:  
                    rslt.append(temp)              
        return rslt