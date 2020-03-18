def containsDuplicates(a):
    cache={}
    for item in a:
        if cache.get(item,None):
            return True
        else:
            cache[item]=1
    return False