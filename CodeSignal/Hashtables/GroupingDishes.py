def groupingDishes(dishes):
    ingredients={}
    res=[]

    for x in range(len(dishes)):
        curr_dish=dishes[x][0]
        for y in range(1,len(dishes[x])):
            if ingredients.get(dishes[x][y],None):
                ingredients[dishes[x][y]].append(curr_dish)
            else:
                ingredients[dishes[x][y]]=[curr_dish]

    for x in sorted(ingredients.keys()):
        if len(ingredients[x])>1:
            res.append([x])
            res[-1].extend(sorted(ingredients[x]))       
    return res