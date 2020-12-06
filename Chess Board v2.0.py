from tkinter import *
import tkinter.font as font

root = Tk()
root.geometry("900x800")
root.title("Chess")

frame = Frame(root)

fontsize = font.Font(size = 20)   # Just for some good Visuals :))

board = [
    [' ','a','b','c','d','e','f','g','h'],
    [8,'♜','♞','♝','♚','♛','♝','♞','♜'],
    [7,'♟','♟','♟','♟','♟','♟','♟','♟'],
    [6,'   ','   ','   ','   ','   ','   ','   ','   '],
    [5,'   ','   ','   ','   ','   ','   ','   ','   '],
    [4,'   ','   ','   ','   ','   ','   ','   ','   '],
    [3,'   ','   ','   ','   ','   ','   ','   ','   '],
    [2,'♙','♙','♙','♙','♙','♙','♙','♙'],
    [1,'♖','♘','♗','♔','♕','♗','♘','♖']
]


# Creating the Chess Board using the above list
def Create_Board():
    global fontsize, frame, board
    temp = label = Label(frame)
    r = c = 0
    for r in range(9):
        for c in range(9):
            if r > 0 and c > 0:
                temp = Label(frame, text = board[r][c], font = fontsize)
                temp.grid(row = r,column = c,ipadx = 30,ipady = 20)
                if r % 2 != 0:
                    if c % 2 != 0:
                        temp.config(bg = '#a6a')
                    else:
                        temp.config(bg = 'white')
                else:
                    if c % 2 != 0:
                        temp.config(bg = 'white')
                    else:
                        temp.config(bg = '#a6a')
            else:
                temp = Label(frame, text = board[r][c], font = fontsize)
                temp.grid(row = r,column = c,ipadx = 25,ipady = 20)


Create_Board()

frame.pack(expand=True)   # Making the Positioning of the Board onto the Center of the window generated.
root.mainloop()
