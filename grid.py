def build_maze(m, n, swag):
    grid = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append("wall")
            grid.append(row)
    return grid

print(build_maze(5, 10, None))