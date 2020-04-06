def nQueens(n):
    res=[]
    curr=[0]*n
    
    if n==1:
        return [[1]]
    elif n==2:
        return [[]]
    elif n==3:
        return [[]]

    def checkQueen(x,curr,col):
        if x not in curr:
            for y in range(col-2,-1,-1):
                if curr[y]!=x+((col-1)-y) and curr[y]!=x-((col-1)-y):
                    return True
        return False

    def findQueens(res,curr,col=1):
        for x in range(1,n+1):
            if checkQueen():
                curr[col]=x
                if col==n:
                    res.append(curr)
                else:
                    findQueens(res,curr,col=col+1)

    return res