def findLiveCells(result, i, j):
    liveCells = 0
    adjacencyMatrix = [(-1,0),(1,0),(0,-1),(0,1),(-1,1),(1,-1),(-1,-1),(1,1)]   #to check top,down,left,right,diagonals
    for k in adjacencyMatrix:
            new_row = i + k[0]
            new_column = j + k[1]
            if (new_row >= 0 and new_column>=0) and (new_row <=(numberOfRows - 1) and new_column <= (numberOfColumns - 1)):
                    if result[new_row][new_column] == '*':
                        liveCells += 1
    return liveCells                    
board = [['.','*','.'],['.','.','*'],['*','*','*'],['.','.','.']]  #"*" represents live cell and "." represents dead cell
numberOfRows = len(board)
numberOfColumns = len(board[0])
result = list()
for i in range(numberOfRows):
    Row = ['.']*numberOfColumns
    for j in range(numberOfColumns):
        liveCells=findLiveCells(board,i,j)
        if board[i][j] == '*':
            if liveCells < 2 or liveCells > 3:
                Row[j] = '.'
            elif liveCells == 3 or liveCells == 2:
                Row[j] = '*'
        elif board[i][j] == '.':
            if liveCells == 3:
                Row[j] = '*'        
    result.append(Row)          
print(result)                                 
