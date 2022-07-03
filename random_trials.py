from grid_2048 import *
from pytest import *
gr= create_grid(5)
grid = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [5, ' ', ' ', 2]]
#grid_add_new_tile_at_position(gr,1,1)

#print(init_game())
aa ="""
 === === === ===
| 0 | 0 | 0 | 0 |
 === === === ===
| 0 | 0 | 0 | 0 |
 === === === ===
| 0 | 0 | 0 | 0 |
 === === === ===
| 2 | 0 | 0 | 2 |
 === === === ===
    """

a ="""
 === === === ===
|   |   |   |   |
 === === === ===
|   |   |   |   |
 === === === ===
|   |   |   |   |
 === === === ===
| 2 |   |   | 2 |
 === === === ===
    """
#[20,54,89,125]
#print (a[1:20] + '5' + a[21:-1])
#print(a[1:24])
#print(grid_to_string(grid,4))
def print_line(n,len_grid):
    if n == 1:
        for _ in range(len_grid):
            print(' ===',end="")
        print(' ', end="\n")
#        print(' === === === === ',end='\n')
    elif n == 2:
        for _ in range(len_grid):
            print(' ====',end="")
        print(' ', end="\n")
#        print(' ==== ==== ==== ==== ',end='\n')
    elif n == 3:
        for _ in range(len_grid):
            print(' =====',end="")
        print(' ', end="\n")
#        print(' ===== ===== ===== ===== ',end='\n')
    elif n == 4:
        for _ in range(len_grid):
            print(' ===',end="")
        print(' ', end="\n")
#        print(' ====== ====== ====== ====== ',end='\n') 
def print_grid(grid):
    m = long_value(grid)
    n = len(grid)
    for i in range(n):
        print_line(m, n)
        for j in range(n):
            ch = str(grid[i][j])
            while (len(ch) < m):
                ch += ' '
            print('| '+ch+' ',end="")
        print ('|',end='\n')
    print_line(m, n)

render_grid(grid)
print(grid_to_string(grid))




