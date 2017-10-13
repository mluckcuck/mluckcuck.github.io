gridOfMines = [["O", "O", "M", "O", "M"],
        ["O", "M", "M", "O", "M"],
        ["O", "O", "M", "M", "O"],
        ["O", "M", "O", "O", "O"],
        ["O", "O", "O", "M", "M"]]


def printGrid(grid):
    for row in grid:
        print(row)

def mineDetector(grid):
    mines = []
    
    for row in range(len(grid)):
        for col in range(len(grid[row])):  
            if grid[row][col] == "M":
                mines.append((row,col))


    return mines


mineList = mineDetector(gridOfMines)
print(mineList)

def buildGrid(mineList):
    grid = [["O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O"]]

    for coord in mineList:
        x,y = coord
        grid[x][y] = "M"


    return grid



gridBack = buildGrid(mineList)

printGrid(gridBack)


