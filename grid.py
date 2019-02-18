from random import randint

def build_maze(m, n, swag):
    grid = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append("wall")
            grid.append(row)
    start_i = randint(0, m - 1)
    start_j = randint(0, n - 1)
    grid[start_i][start_j] = "start"
    mow(grid, start_i, start_j)
    return grid

def print_maze(grid):
    for row in grid:
        printable_row = ''
        for cell in row:
            if cell == "wall":
                char = '|'
            else:
                char = ' '
            printable_row += char
        print(printable_row)

def mow(grid, i, j):
    directions = ['U','D','L','R']
    while len(directions) > 0:
        directions_index = randint(0, len(directions)-1)
        direction = directions.pop(directions_index)

        if direction == 'U':
            if i - 2 < 0:
                continue
            elif grid[i - 2][j] == 'wall':
                grid[i - 1][j] = 'empty'
                grid[i - 2][j] = 'empty'
                mow(grid, i - 2, j)
        
        elif direction == 'D':
            if i + 2 >= len(grid):
                continue
            elif grid[i + 2][j] == 'wall':
                grid[i + 1][j] = 'empty'
                grid[i + 2][j] = 'empty'
                mow(grid, i + 2, j)
        
        elif direction == 'L':
            if j - 2 < 0:
                continue
            elif grid[i][j - 2] == 'wall':
                grid[i][j - 1] = 'empty'
                grid[i][j - 2] = 'empty'
                mow(grid, i, j - 2)
        
        else:
            if j + 2 >= len(grid[0]):
                continue
            elif grid[i][j + 2] == 'wall':
                grid[i][j + 1] = 'empty'
                grid[i][j + 2] = 'empty'
                mow(grid, i, j + 2)

def explore_maze(grid, start_i, start_j, swag):
    grid_copy = [row[:] for row in grid]
    bfs_queue = [[start_i, start_j]]
    directions = ['U', 'D', 'L', 'R']
    while bfs_queue:
        i, j = bfs_queue.pop(0)
        

print_maze(build_maze(5, 10, None))