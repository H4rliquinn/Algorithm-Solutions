def firstNotRepeatingCharacter(s):
    found=set()
    unrepeated=[]
    for char in s:
        if char not in found:
            found.add(char)
            unrepeated.append(char)
        elif char in unrepeated:
            unrepeated.remove(char)

    if len(unrepeated)>0:
        return unrepeated[0]
    else:
        return '_'