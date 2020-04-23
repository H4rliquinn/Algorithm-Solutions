def groupingDishes(dishes):
    ingredients={}
    ingredient_list=[]

    for x in range(len(dishes)):
        curr_dish=dishes[x][0]
        for y in range(1,len(dishes[x])):
            if ingredients.get(dishes[x][y],None):
                ingredients[dishes[x][y]].append(curr_dish)
            else:
                ingredients[dishes[x][y]]=[curr_dish]

    print(ingredients)