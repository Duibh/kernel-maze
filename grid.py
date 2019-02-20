from random import randint
from collections import defaultdict, deque
from heapq import heappush, heappop
import operator

def build_maze(m, n, swag):
    grid = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append("wall")
        grid.append(row)
    start_i = randint(0, m-2)
    start_j = randint(0, n-2)
    grid[start_i][start_j] = 'Start'
    mow(grid, start_i, start_j)
    end_i, end_j = explore_maze(grid, start_i, start_j, swag)
    a_star(grid, (start_i, start_j), (end_i, end_j), swag)
    return grid

def print_maze(grid):
    for row in grid:
        printable_row = ''
        for cell in row:
            if cell == 'wall':
                char = '|'
            elif cell == 'empty':
                char = ' '
            else:
                char = cell[0]
            printable_row += char
        print(printable_row)

def mow(grid, i, j):
    directions = ['U','D','L','R']
    while(len(directions) > 0):
        directions_index = randint(0, len(directions)-1)
        direction = directions.pop(directions_index)

        if direction == 'U':
            if i - 2 < 1:
                continue
            elif grid[i - 2][j] == 'wall':
                grid[i - 1][j] = 'empty'
                grid[i - 2][j] = 'empty'
                mow(grid, i - 2, j)
        
        elif direction == 'D':
            if i + 2 >= len(grid)-1:
                continue
            elif grid[i + 2][j] == 'wall':
                grid[i + 1][j] = 'empty'
                grid[i + 2][j] = 'empty'
                mow(grid, i + 2, j)
        
        elif direction == 'L':
            if j - 2 < 1:
                continue
            elif grid[i][j - 2] == 'wall':
                grid[i][j - 1] = 'empty'
                grid[i][j - 2] = 'empty'
                mow(grid, i, j - 2)
        
        else:
            if j + 2 >= len(grid[0]) -1:
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
        if grid[i][j] != 'Start' and randint(1,10) == 1:
            grid[i][j] = swag[randint(0, len(swag)-1)]
        grid_copy[i][j] = 'visited'
        for direction in directions:
            explore_i = i
            explore_j = j
            if direction == 'U':
                explore_i = i - 1
            elif direction == 'D':
                explore_i = i + 1
            elif direction == 'L':
                explore_j = j - 1
            else:
                explore_j = j + 1
            
            if explore_i < 0 or explore_j < 0 or explore_i >= len(grid) or explore_j >= len(grid[0]):
                continue
            elif grid_copy[explore_i][explore_j] != 'visited' and grid_copy[explore_i][explore_j] != 'wall':
                bfs_queue.append([explore_i, explore_j])
                
    grid[i][j] = 'End'
    return i, j

def heuristic(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

def a_star(grid, start, end, swag):
    neighbors = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
    close_set = set()
    came_from = {}
    gscore = {start:0}
    fscore = {start:heuristic(start, end)}
    oheap = []
    heappush(oheap, (fscore[start], start))
    swag_collection = defaultdict(int)
    while oheap:
        current = heappop(oheap)[1]
        if current == end:
            data = []
            while current in came_from:
                i, j = current
                if grid[i][j] != 'End':
                    if grid[i][j] in swag:
                        swag_collection[grid[i][j]] += 1
                    grid[i][j] = '.'
                data.insert(0, current)
                current = came_from[current]
            if swag_collection:
                print('Swag:')
                for key, value in sorted(swag_collection.items(), key=operator.itemgetter(1)) :
                    print('\t{0} - {1}'.format(key, value))
            else:
                print('No swag!')
            return data
        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + heuristic(current, neighbor)
            if 0 <= neighbor[0] < len(grid):
                if 0 <= neighbor[1] < len(grid[0]):
                    if grid[neighbor[0]][neighbor[1]] == 'wall':
                        continue
                else:
                    continue
            else:
                continue
            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue
            if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, end)
                heappush(oheap, (fscore[neighbor], neighbor))

print_maze(build_maze(15, 30, ['candy', 'werewolf', 'pumpkin']))