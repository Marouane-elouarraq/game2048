import random as rd
from textual_2048 import *
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

mouvement = ['left', 'right', 'up', 'down']


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


def print_line(n, len_grid):
    if n == 1:
        for _ in range(len_grid):
            print(' ===', end="")
        print(' ', end="\n")
#        print(' === === === === ',end='\n')
    elif n == 2:
        for _ in range(len_grid):
            print(' ====', end="")
        print(' ', end="\n")
#        print(' ==== ==== ==== ==== ',end='\n')
    elif n == 3:
        for _ in range(len_grid):
            print(' =====', end="")
        print(' ', end="\n")
#        print(' ===== ===== ===== ===== ',end='\n')
    elif n == 4:
        for _ in range(len_grid):
            print(' ===', end="")
        print(' ', end="\n")
#        print(' ====== ====== ====== ====== ',end='\n')


def grid_to_string(grid):
    m = long_value(grid)
    n = len(grid)
    for i in range(n):
        print_line(m, n)
        for j in range(n):
            ch = str(grid[i][j])
            while (len(ch) < m):
                ch += ' '
            print('| '+ch+' ', end="")
        print('|', end='\n')
    print_line(m, n)


def squeez(row):
    n = len(row)
    all_values = []
    for x in row:
        if x != 0:
            all_values.append(x)
    while len(all_values) < n:
        all_values.append(0)
    return all_values


def move_row_left(row):
    n = len(row)
    squeezed_row = squeez(row)
    for i in range(0, n-1):
        if squeezed_row[i] == squeezed_row[i+1]:
            squeezed_row[i] = 2*squeezed_row[i]
            squeezed_row[i+1] = 0
    return squeez(squeezed_row)


def move_row_right(row):
    alt_row = [x for x in row]
    alt_row.reverse()
    l = move_row_left(alt_row)
    l.reverse()
    return l


def transpose(grid):
    n = len(grid)
    tran_grid = []
    for i in range(n):
        t = [l[i] for l in grid]
        tran_grid.append(t)
    return tran_grid


def move_grid(grid, d):
    new_grid = []
    if d == 'left':
        for l in grid:
            new_grid.append(move_row_left(l))
    if d == 'right':
        for l in grid:
            new_grid.append(move_row_right(l))
    if d == 'up':
        for l in transpose(grid):
            new_grid.append(move_row_left(l))
        new_grid = transpose(new_grid)
    if d == 'down':
        for l in transpose(grid):
            new_grid.append(move_row_right(l))
        new_grid = transpose(new_grid)
    return new_grid


def is_grid_full(grid):
    tiles = get_all_tiles(grid)
    return (not 0 in tiles)


def move_possible(grid):
    mv_possible = []
    mv_possible.append(move_grid(grid, 'left') != grid)
    mv_possible.append(move_grid(grid, 'right') != grid)
    mv_possible.append(move_grid(grid, 'up') != grid)
    mv_possible.append(move_grid(grid, 'down') != grid)
#    mv_possible = [move_grid(grid, 'left') != grid, move_grid(grid, 'right') != grid, move_grid(grid, 'up') != grid, move_grid(grid, 'down') != grid]
    return mv_possible


def mvt_possible(grid):
    mv_possible = []
    n = len(grid)
    bool_possible = move_possible(grid)
    for i in range(n):
        if bool_possible[i]:
            mv_possible.append(mouvement[i])
    return mv_possible


def is_game_over(grid):
    if move_possible(grid) == [False, False, False, False]:
        return True
    else:
        return False


def is_game_won(grid):
    render_grid(grid)
    tiles = get_all_tiles(grid)
    for x in tiles:
        if x > 2048:
            return True
    return False


def random_play():
    grid = init_game()
    render_grid(grid)
    print(grid_to_string(grid))
    while (not is_game_over(grid)):

        mv = rd.choice(mvt_possible(grid))
        grid = move_grid(grid, mv)
        grid = grid_add_new_tile(grid)
        print (grid_to_string(grid))
    if is_game_won(grid):
        print('you won')
    else:
        print('you lost')

def game_play():
    n = int(read_size_grid())
    grid = init_game(n)
    render_grid(grid)
    print(grid_to_string(grid))
    while (not is_game_over(grid)):
        mv = read_player_command()
        if mv == 'g':
            mv = 'left'
        elif mv == 'd':
            mv = 'right'
        elif mv == 'h':
            mv = 'up'
        elif mv == 'b':
            mv = 'down'
        elif mv == 'x':
            break
        grid = move_grid(grid, mv)
        grid = grid_add_new_tile(grid)
        print (grid_to_string(grid))
