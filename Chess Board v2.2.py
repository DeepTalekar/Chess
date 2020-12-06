from tkinter import *
import tkinter.font as font


root = Tk()
# root.attributes("-fullscreen",True) # For Full Screen Window without Option (i.e. Close, Restore, & Minimize) 

monitor_width = root.winfo_screenwidth()
monitor_height = root.winfo_screenheight()
root.geometry("%dx%d" % (monitor_width, monitor_height))

myFont = font.Font(family="Courier",size=20,weight="bold")

fontsize = font.Font(size = 20)     # Just for Some good Visuals :))

labelfont = font.Font(family = "Arial", size = 15, weight = "bold")

buttonfont = font.Font(family = "Courier", size = 15, weight = "bold")

root.title("Chess")

frame = Frame(root)

moveInput = Frame(root)

container1 = Frame(moveInput)
container2 = Frame(moveInput)

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

# Logic behind Creating the Chess Board using the above list
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


Create_Board()  # Creating the Chess Board

Label(moveInput, text = "Enter the Row and Column Below to Make a Move", font = myFont, fg = '#4169e1').pack(side = TOP, expand = True, pady = 30)

# For Row Input 
Label(container1, text = "Initial Row Index:", font = labelfont, fg = '#007bff').pack(side = 'left', expand = True, padx = 10, pady = 20)
initialrowInput = Entry(container1, font = labelfont, fg = '#28a745')
initialrowInput.pack(side = LEFT, expand = True, padx = 10, pady = 20)

finalrowInput = Entry(container1, font = labelfont, fg = '#28a745')
finalrowInput.pack(side = RIGHT, expand = True, padx = 10, pady = 20)
Label(container1, text = "Final Row Index:", font = labelfont, fg = '#007bff').pack(side = RIGHT, expand = True, padx = 10, pady = 10)

# For Column Input
Label(container2, text = "Initial Column Letter:", font = labelfont, fg = '#007bff').pack(side = 'left', expand = True, padx = 10, pady = 10)
initialcolumnInput = Entry(container2, font = labelfont, fg = '#28a745')
initialcolumnInput.pack(side = LEFT, expand = True, padx = 10, pady = 10)

finalcolumnInput = Entry(container2, font = labelfont, fg = '#28a745')
finalcolumnInput.pack(side = RIGHT, expand = True, padx = 10, pady = 10)
Label(container2, text = "Final Column Letter:", font = labelfont, fg = '#007bff').pack(side = RIGHT, expand = True, padx = 10, pady = 10)

# Submit Move via Button
submitMove = Button(moveInput, text = 'Submit', font = buttonfont, fg = '#800080', bg = '#ffc107', borderwidth = 0)
submitMove.pack(side = BOTTOM, expand = True, ipadx = 5, ipady = 5, pady = 5)

frame.pack(expand=True) # Making the Positioning of the Board onto the Center of the window generated.
moveInput.pack(expand = True, side = 'bottom')
container1.pack(expand = True, side = 'bottom', pady = 10, fill = X)
container2.pack(expand = True, side = 'bottom', pady = 10, fill = X)

root.mainloop()
