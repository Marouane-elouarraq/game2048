from grid_2048 import *
from pytest import *
gr= create_grid(4)
grid_add_new_tile_at_position(gr,1,1)

print(init_game())