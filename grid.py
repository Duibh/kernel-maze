from random import randint

def build_maze(m, n, swag):
    grid = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append("wall")
            grid.append(row)
    start_i = randint(0, m-1)
    start_j = randint(0, n-1)
    grid[start_i][start_j] = "empty"
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

print_maze(build_maze(5, 10, None))