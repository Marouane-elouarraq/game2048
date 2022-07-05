from tkinter import *
from grid_2048 import *

def graphical_grid_init():
    root = Tk()
    root.title("2048")
    top = Toplevel()
    top.grid()

    background = Frame(root)
    background.pack()

    C = Canvas(background, bg='#8B7D6B')

    C.create_line(0, 65, 1000, 65, fill='#CDB79E')
    C.create_line(0, 130, 1000, 130, fill='#CDB79E')
    C.create_line(0, 195, 1000, 195, fill='#CDB79E')

    #C.create_text(48, 40, text="H", fill="black", font=('Helvetica 15 bold'))
    #C.create_text(144, 40, text="H", fill="black", font=('Helvetica 15 bold'))
    #C.create_text(240, 40, text="H", fill="black", font=('Helvetica 15 bold'))
    #C.create_text(336, 40, text="H", fill="black", font=('Helvetica 15 bold'))

    C.create_line(95, 0, 95, 1000, fill='#CDB79E')
    C.create_line(190, 0, 190, 1000, fill='#CDB79E')
    C.create_line(285, 0, 285, 1000, fill='#CDB79E')
    
    return (top,C)



def display_and_update(grid):
    #grid = init_game()
    render_grid(grid)
    C = graphical_grid_init()[1]
    top = graphical_grid_init()[0]

    C.create_text(48, 40, text=str(
        grid[0][0]), fill="black", font=('Helvetica 15 bold'))
    C.create_text(144, 40, text=str(
        grid[0][1]), fill="black", font=('Helvetica 15 bold'))
    C.create_text(240, 40, text=str(
        grid[0][2]), fill="black", font=('Helvetica 15 bold'))
    C.create_text(336, 40, text=str(
        grid[0][3]), fill="black", font=('Helvetica 15 bold'))

    C.create_text(48, 95, text=str(
        grid[1][0]), fill="black", font=('Helvetica 15 bold'))
    C.create_text(144, 95, text=str(
        grid[1][1]), fill="black", font=('Helvetica 15 bold'))
    C.create_text(240, 95, text=str(
        grid[1][2]), fill="black", font=('Helvetica 15 bold'))
    C.create_text(336, 95, text=str(
        grid[1][3]), fill="black", font=('Helvetica 15 bold'))

    C.create_text(48, 160, text=str(
        grid[2][0]), fill="black", font=('Helvetica 15 bold'))
    C.create_text(144, 160, text=str(
        grid[2][1]), fill="black", font=('Helvetica 15 bold'))
    C.create_text(240, 160, text=str(
        grid[2][2]), fill="black", font=('Helvetica 15 bold'))
    C.create_text(336, 160, text=str(
        grid[2][3]), fill="black", font=('Helvetica 15 bold'))

    C.create_text(48, 230, text=str(
        grid[3][0]), fill="black", font=('Helvetica 15 bold'))
    C.create_text(144, 230, text=str(
        grid[3][1]), fill="black", font=('Helvetica 15 bold'))
    C.create_text(240, 230, text=str(
        grid[3][2]), fill="black", font=('Helvetica 15 bold'))
    C.create_text(336, 230, text=str(
        grid[3][3]), fill="black", font=('Helvetica 15 bold'))

    C.pack()
    top.mainloop()

#def key_pressed(event):
#    ch = ''
#    if event == '<g>':
#        ch = 'left'
#    if event == '<d>':
#        ch = 'right'
#    if event == '<h>':
#        ch = 'up'
#    if event == '<b>':
#        ch = 'down'
#    return ch
def key_p(event):
    #display_and_update(grid)
    print('h')
def graphical_game_play():

    grid = init_game()
    render_grid(grid)

    #print(grid_to_string(grid))
    C = graphical_grid_init()[1]
    top = graphical_grid_init()[0]
    top.mainloop()

    


    C.bind("<1>", lambda event: C.focus_set())
    
    C.bind('<a>', key_p)
        #mv = read_player_command()
    #if mv == 'g':
    #    mv = 'left'
    #elif mv == 'd':
    #    mv = 'right'
    #elif mv == 'h':
    #    mv = 'up'
    #elif mv == 'b':
    #    mv = 'down'
    #elif mv == 'x':
    #    break
    #grid = move_grid(grid, mv)
    #grid = grid_add_new_tile(grid)
    C.pack()
    top.mainloop()

graphical_game_play()