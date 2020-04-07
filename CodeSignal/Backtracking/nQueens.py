def nQueens(n):
    res=[]
    curr=[0]*n
    
    if n==1:
        return [[1]]
    elif n in [2,3]:
        return []

    def checkQueen(x,col,curr):
        # print("STOP",x,col,curr)
        if col==1:
            return True
        if x in curr:
            return False
        flag=True
        for y in range(col-2,-1,-1):
            # print("Diag",curr,col,y,x,((col-1)-y))
            # print (curr[y],curr[y]==x+((col-1)-y),curr[y]==x-((col-1)-y))
            if curr[y]==x+((col-1)-y) or curr[y]==x-((col-1)-y):
                # print("!")
                flag=False

        # print("End")
        return flag

    def findQueens(res,curr,col=1):
        for x in range(1,n+1):
            if checkQueen(x,col,curr):
                curr[col-1]=x
                if col==n:
                    print("LAST")
                    if not checkQueen(x,col,curr):
                        res.append(list(curr))
                else:
                    new_curr=list(curr)
                    findQueens(res,new_curr,col=col+1)
    findQueens(res,curr)
    return res
