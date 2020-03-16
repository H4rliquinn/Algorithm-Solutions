def isCryptSolution(crypt, solution):
    #Create a solution key
    sol={}
    for i in solution:
        sol[i[0]]=i[1]
    nums=[0,0,0]

    for x in range(3):
        n=''
        # print(crypt)
        for char in crypt[x]:
            decrypt=sol[char]
            if n=='0':
                return False
            n+=decrypt
        nums[x]=n
    
    #test if valid
    print("NUMS",nums)
    if int(nums[0])+int(nums[1])==int(nums[2]):
        return True
    else:
        return False