# mlproject/lib.py


def sudoku_validator(grid):
    bool_check=check_col(grid)
    bool_check= bool_check and check_row(grid)
    bool_check=bool_check and check_square(grid)
    return bool_check

def check_col(grid):
    numbers=[1,2,3,4,5,6,7,8,9]
    for i in range(0,len(grid)):
        col=[]
        for j in range(0,len(grid)):
            col.append(grid[j][i])
        if sorted(col)!=numbers:
            return False
    return True

def check_row(grid):
    numbers=[1,2,3,4,5,6,7,8,9]
    for i in grid:
        if sorted(i)!=numbers:
            return False
    return True

def check_square(grid):
    result=True
    result=fill_square(grid,(0,2),(0,2))
    result=result and fill_square(grid,(3,5),(0,2))
    result=result and fill_square(grid,(6,8),(0,2))
    result=result and fill_square(grid,(0,2),(3,5))
    result=result and fill_square(grid,(3,5),(3,5))
    result=result and fill_square(grid,(6,8),(3,5))
    result=result and fill_square(grid,(0,2),(6,8))
    result=result and fill_square(grid,(3,5),(6,8))
    result=result and fill_square(grid,(6,8),(6,8))
    return result

def fill_square(grid,row_coord,col_coord):
    square=[]
    numbers=[1,2,3,4,5,6,7,8,9]
    for i in range(row_coord[0],row_coord[1]+1):
        for j in range(col_coord[0],col_coord[1]+1):
            square.append(grid[i][j])
    print(sorted(square))
    if sorted(square)!=numbers:
        return False
    return True

