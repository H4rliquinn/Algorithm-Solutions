def sudoku2(grid):
    #Test Columns
    for col in grid:
        col=[i for i in col if i!='.']
        if len(col)!=len(set(col)):
            return False
    #Test Rows
    for x in range(9):
        row=[]
        for y in range(9):
            row.append(grid[y][x])
        row=[i for i in row if i!='.']
        if len(row)!=len(set(row)):
            return False   
    #Test Boxes
    for z in range(3):
        for q in range(3):
            box=[]
            for y in range(z*3,(z*3)+3):
                for x in range(q*3,(q*3)+3):
                    box.append(grid[y][x])
                    box=[i for i in box if i!='.']
                    if len(box)!=len(set(box)):
                        return False  
    return True