def rotateImage(a):
    size=len(a)
    for i in range(size//2): 
        for j in range(i, size-i-1): 
            temp = a[i][j] 
            a[i][j] = a[size-j-1][i] 
            a[size-j-1][i] = a[size-i-1][size-j-1] 
            a[size-i-1][size-j-1] = a[j][size-i-1] 
            a[j][size-i-1] = temp 
    return a