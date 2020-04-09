#Kadane's Algorithm
def arrayMaxConsecutiveSum2(inputArray):
    current=float("-inf")
    max_value=float("-inf")
    for x in range(len(inputArray)):
        current=max(inputArray[x],inputArray[x]+current)      
        if current>max_value:
            max_value=current
    return max_value