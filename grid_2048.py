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
