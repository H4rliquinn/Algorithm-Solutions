def sumOfTwo(a, b, v):
    cache={}
    for item in b:
            cache[v-item]=item
    print(cache)   
    for add in a:
        if cache.get(add,None):
            return True
    return False