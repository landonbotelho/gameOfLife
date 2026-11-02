import random


def generateGrid(rows, columns):
    grid = []
    for i in range (0,rows):
        row = []
        for j in range (0, columns):
            row.append(random.randint(0,1))
        grid.append(row)
    return grid

def generateNewGrid(rows, columns):
    newGrid = []
    for i in range(0, rows):
        newGrid.append([0] * columns)
    return newGrid


def displayGrid(grid):
    for row in grid:
        for item in row:
            print("| " + str(item) + ' ', end='')
        print("|\n")


def basicUpdateGrid(grid):
    for i, row in enumerate(grid):
        for j, item in enumerate(row):
            if item == 0:
                grid[i][j] = 1
    return grid



def analyzeNeighbors(grid):
    numRows = len(grid)
    numCols = len(grid[0])
    newGrid = generateNewGrid(numRows, numCols)

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):

            countOfAliveNeighbors = 0

            for x in range (-1,2):
                for y in range (-1,2):
                    if x == 0 and y == 0:
                        continue


                    neighboringRow = i + x
                    neighboringCol = j + y

                    #bypasses if calculated neighbor is in out of bounds location
                    if neighboringRow < 0 or neighboringCol < 0 or neighboringRow >= numRows or neighboringCol >= numCols:
                        continue

                    if grid[neighboringRow][neighboringCol] == 1:
                        countOfAliveNeighbors += 1

            #dies
            if countOfAliveNeighbors < 2:
                newGrid[i][j] = 0
            #survives
            elif countOfAliveNeighbors >= 2 and countOfAliveNeighbors <= 3 and grid[i][j] == 1:
                newGrid[i][j] = 1
            #overpopulates
            elif countOfAliveNeighbors > 3 and grid[i][j] == 1:
                newGrid[i][j] = 0
            #reproduces    
            elif countOfAliveNeighbors == 3 and grid[i][j] == 0:
                newGrid[i][j] = 1
            
    return newGrid



def start(rows, columns, numOfIterations):
    # Initialize grid
    print("World: Iteration 0")
    currentGrid = generateGrid(rows, columns)
    displayGrid(currentGrid)
    for iterations in range (0,numOfIterations):
        # Update grid
        currentGrid = analyzeNeighbors(currentGrid)
        # Display initial grid
        print("World: Iteration " + str(iterations+1))
        displayGrid(currentGrid)
        print("\n\n")




start(5,5,8)