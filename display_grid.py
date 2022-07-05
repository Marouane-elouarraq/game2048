from tkinter import *
from grid_2048 import *

def key_pressed(event):
    print('hello')
def graphical_grid_init():
    grid = init_game()
    render_grid(grid)
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

    # C.create_rectangle(5, 5, 95, 65, fill="#8B7D6B")
#     C.create_rectangle(100, 5, 185, 65, fill="#8B7D6B")
#     C.create_rectangle(190, 5, 275, 65, fill="#8B7D6B")
#     C.create_rectangle(280, 5, 370, 65, fill="#8B7D6B")

#     C.create_rectangle(5, 70, 95, 130, fill="#8B7D6B")
#     C.create_rectangle(100, 70, 185, 130, fill="#8B7D6B")
#     C.create_rectangle(190, 70, 275, 130, fill="#8B7D6B")
#     C.create_rectangle(280, 70, 370, 130, fill="#8B7D6B")

#     C.create_rectangle(5, 135, 95, 185, fill="#8B7D6B")
#     C.create_rectangle(100, 135, 185, 185, fill="#8B7D6B")
#     C.create_rectangle(190, 135, 275, 185, fill="#8B7D6B")
#     C.create_rectangle(280, 135, 370, 185, fill="#8B7D6B")

#     C.create_rectangle(5, 190, 95, 240, fill="#8B7D6B")
#     C.create_rectangle(100, 190, 185, 240, fill="#8B7D6B")
#     C.create_rectangle(190, 190, 275, 240, fill="#8B7D6B")
#     C.create_rectangle(280, 190, 370, 240, fill="#8B7D6B")

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

    C.bind("<1>", lambda event: C.focus_set())
    C.bind('<a>', )

    C.pack()

    top.mainloop()


#grid = [[2, 0, 0, 2], [2, 4, 0, 0], [8, 4, 2, 0], [8, 2, 2, 0]]
#graphical_grid_init()

