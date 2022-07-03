import random as rd


def create_grid(n=4):
    s = []
    for i in range(0, n):
        t = []
        for j in range(0, n):
            t.append(' ')
        s.append(t)
    return s


def grid_add_new_tile_at_position(grid, x, y):
    to_add = rd.choice([2, 4])
    grid[x][y] = to_add


def get_all_tiles(grid):
    all_tiles = []
    for l in grid:
        for x in l:
            if x == ' ':
                all_tiles.append(0)
            else:
                all_tiles.append(x)
    return all_tiles


def get_empty_tiles_positions(grid):
    empty_pos = []
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == ' ' or grid[i][j] == 0:
                empty_pos.append((i, j))
    return empty_pos


def get_new_position(grid):
    empty_pos = get_empty_tiles_positions(grid)
    return rd.choice(empty_pos)


def grid_get_value(grid, x, y):
    if grid[x][y] == ' ':
        return 0
    return grid[x][y]


def grid_add_new_tile(grid):
    empty_pos = get_empty_tiles_positions(grid)
    x, y = rd.choice(empty_pos)
    to_add = rd.choice([2,4])
    grid[x][y] = to_add
    return grid

def init_game(n = 4):
    grid = create_grid(n)
    grid = grid_add_new_tile(grid)
    grid = grid_add_new_tile(grid)
    return grid