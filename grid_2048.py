import random as rd
a1 = """
 === === === ===
|   |   |   |   |
 === === === ===
|   |   |   |   |
 === === === ===
|   |   |   |   |
 === === === ===
|   |   |   |   |
 === === === ===
    """
a2 = """
 ==== ==== ==== ====
|    |    |    |    |
 ==== ==== ==== ====
|    |    |    |    |
 ==== ==== ==== ====
|    |    |    |    |
 ==== ==== ==== ====
|    |    |    |    |
 ==== ==== ==== ====
    """
dict_a = {1: a1, 2: a2}


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
    to_add = rd.choice([2, 4])
    grid[x][y] = to_add
    return grid


def init_game(n=4):
    grid = create_grid(n)
    grid = grid_add_new_tile(grid)
    grid = grid_add_new_tile(grid)
    return grid


def render_grid(grid):
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == ' ':
                grid[i][j] = 0


def grid_to_string_(grid, n):
    render_grid(grid)
    m = long_value(grid)
    a = dict_a[m]
    displayed = a[0:20] + str(grid[0][0]) + a[21:]
    displayed = displayed[0:24] + str(grid[0][1]) + displayed[25:]
    displayed = displayed[0:28] + str(grid[0][2]) + displayed[29:]
    displayed = displayed[0:32] + str(grid[0][3]) + displayed[33:]
    displayed = displayed[0:55] + str(grid[1][0]) + displayed[56:]
    displayed = displayed[0:59] + str(grid[1][1]) + displayed[60:]
    displayed = displayed[0:63] + str(grid[1][2]) + displayed[64:]
    displayed = displayed[0:67] + str(grid[1][3]) + displayed[68:]
    displayed = displayed[0:90] + str(grid[2][0]) + displayed[91:]
    displayed = displayed[0:94] + str(grid[2][1]) + displayed[95:]
    displayed = displayed[0:98] + str(grid[2][2]) + displayed[99:]
    displayed = displayed[0:102] + str(grid[2][3]) + displayed[103:]
    displayed = displayed[0:125] + str(grid[3][0]) + displayed[126:]
    displayed = displayed[0:129] + str(grid[3][1]) + displayed[130:]
    displayed = displayed[0:133] + str(grid[3][2]) + displayed[134:]
    displayed = displayed[0:137] + str(grid[3][3]) + displayed[138:]
    return (displayed)


def long_value(grid):
    length_grid = []
    render_grid(grid)
    for l in grid:
        for x in l:
            length_grid.append(len(str(x)))
    return max(length_grid)


def print_line(n):
    if n == 1:
        print(' === === === === ', end='\n')
    elif n == 2:
        print(' ==== ==== ==== ==== ', end='\n')
    elif n == 3:
        print(' ===== ===== ===== ===== ', end='\n')
    elif n == 4:
        print(' ====== ====== ====== ====== ', end='\n')


def grid_to_string(grid):
    m = long_value(grid)
    n = len(grid)
    for i in range(n):
        print_line(m)
        for j in range(n):
            ch = str(grid[i][j])
            while (len(ch) < m):
                ch += ' '
            print('| '+ch+' ',end="")
        print ('|',end='\n')
    print_line(m)


