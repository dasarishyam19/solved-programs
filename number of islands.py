def numIslands(grid):
    def dfs(ith_row, jth_column):
        grid[ith_row][jth_column] = "2"
        m = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for move in m:
            next_row = ith_row + move[0]
            next_column = jth_column + move[1]
            if 0 <= next_row < number_of_rows and 0 <= next_column < number_of_columns and grid[next_row][next_column] == "1":
                dfs(next_row, next_column)

    number_of_rows = len(grid)
    number_of_columns = len(grid[0])
    number_of_islands = 0

    for i in range(number_of_rows):
        for j in range(number_of_columns):
            if grid[i][j] == "1":
                number_of_islands += 1
                dfs(i, j)

    return number_of_islands
    
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
       ]
print(numIslands(grid))
    