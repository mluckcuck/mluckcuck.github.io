import json

def loadGrid(fileName):
    
    
    try:
        gridFile = open(fileName)
        grid = json.load(gridFile)
    except OSError as err:
        print("File Not Found")
        print(err)
        #Then do something useful
         #Perhaps ask the user for the file name?
        return []
    except json.decoder.JSONDecodeError as err:
        print("Grid File Invalid")
        print(err)
        gridFile.close()
        return []
    else:
        gridFile.close()
        return grid

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

grid = loadGrid("grid.json")

mineList = mineDetector(grid)
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

def saveGrid(grid, fileName):
    try:
        gridFile = open(fileName,"w")
        json.dump(grid, gridFile)
    except FileNotFoundError as err:
        print("File Not Found")
        print(err)
        gridFile.close()
        #Then do something useful
         #Perhaps ask the user for the file name?
    else:
        gridFile.close()
           
   
gridBack = buildGrid(mineList)

printGrid(gridBack)

saveGrid(gridBack, "gridBack.json")    
