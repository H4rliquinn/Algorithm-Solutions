def firstDuplicate(a):
    found=set()
    for x in a:
        if x in found:
            return x
        found.add(x)
    return -1