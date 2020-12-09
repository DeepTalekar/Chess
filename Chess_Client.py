from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import socket
from threading import Thread

''' ******************** Client Part Start ********************* '''

host = 'localhost'
port = 8091

conn = socket.socket()
conn.connect((host, port))

def sendMoveDetails(movedata):
    print("Inside sendMoveDetails!!")
    d1 = dict(movedata)
    print("The Dictionary that we catched -->", d1)
    separator = ', '
    s1 = str(d1)
    print("The string of the above list is --> ", s1)

    s1 = s1.encode()
    conn.send(s1)

def quit(event):
    if messagebox.askyesno('Confirm - Want to Quit the Game ?', 'Do You really want to Quit the Game ?'):
        conn.send("q".encode())
        receiver.join()   # To make this thread end first and then Quit the Game
        conn.close()

def Reciever():
    global conn
    move = conn.recv(1024)
    move = move.decode()
    while move != "You just quitted the Game":
        print("Server Echoing {}".format(move))
        move = conn.recv(1024)
        move = move.decode()
    conn.close()
    root.quit()

receiver = Thread(target=Reciever)    # Made a Reciever thread to read the data sent by other clients
receiver.start()

def entryText(event):
    global initialcolumnInput, initialrowInput, finalcolumnInput, finalrowInput
    initcolumn = initialcolumnInput.get()
    initcolumn = initcolumn.lower()
    initrow = initialrowInput.get()
    initrow = initrow.lower()
    finalrow = finalrowInput.get()
    finalrow = finalrow.lower()
    finalcolumn = finalcolumnInput.get()
    finalcolumn = finalcolumn.lower()
    print("Message from the Init column textfiled --> ", initcolumn)
    print("Message from the Init row textfiled --> ", initrow)
    print("Message from the Final column textfiled --> ", finalcolumn)
    print("Message from the Final row textfiled --> ", finalrow)

    moveDict = { 'ic' : initcolumn, 'ir' : initrow, 'fc' : finalcolumn, 'fr' : finalrow }

    sendMoveDetails(moveDict)

    initialcolumnInput.delete(0,END)
    initialrowInput.delete(0,END)
    finalcolumnInput.delete(0,END)
    finalrowInput.delete(0, END)

''' ******************** Client Part End ********************* '''
root = Tk()

monitor_width = root.winfo_screenwidth()
monitor_height = root.winfo_screenheight()
root.geometry("%dx%d" % (monitor_width, monitor_height))

myFont = font.Font(family="Courier",size=20,weight="bold")

labelfont = font.Font(family = "Arial", size = 15, weight = "bold")
fontsize = font.Font(size = 20)     # Just for Some good Visuals :))
buttonfont = font.Font(family = "Courier", size = 15, weight = "bold")

root.title("Chess")

frame = Frame(root)

moveInput = Frame(root)

container1 = Frame(moveInput)
container2 = Frame(moveInput)
container3 = Frame(moveInput)

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

Label(moveInput, text = "Enter the Row and Column Below to Make a Move", font = myFont, fg = '#4169e1').pack(side = TOP, expand = True, pady = 10)

# For Row Input 
Label(container1, text = "Initial Row Index:", font = labelfont, fg = '#007bff').pack(side = 'left', expand = True, padx = 10, pady = 20)
initialrowInput = Entry(container1, font = labelfont, fg = '#28a745', justify = 'center')
initialrowInput.pack(side = LEFT, expand = True, padx = 10, pady = 20)

finalrowInput = Entry(container1, font = labelfont, fg = '#28a745', justify = 'center')
finalrowInput.pack(side = RIGHT, expand = True, padx = 10, pady = 20)
Label(container1, text = "Final Row Index:", font = labelfont, fg = '#007bff').pack(side = RIGHT, expand = True, padx = 10, pady = 10)

# For Column Input
Label(container2, text = "Initial Column Letter:", font = labelfont, fg = '#007bff').pack(side = 'left', expand = True, padx = 10, pady = 10)
initialcolumnInput = Entry(container2, font = labelfont, fg = '#28a745', justify = 'center')
initialcolumnInput.pack(side = LEFT, expand = True, padx = 10, pady = 10)

finalcolumnInput = Entry(container2, font = labelfont, fg = '#28a745', justify = 'center')
finalcolumnInput.pack(side = RIGHT, expand = True, padx = 10, pady = 10)
Label(container2, text = "Final Column Letter:", font = labelfont, fg = '#007bff').pack(side = RIGHT, expand = True, padx = 10, pady = 10)

# Submit Move via Button
submitMove = Button(container3, text = 'Submit', font = buttonfont, fg = '#800080', bg = '#ffc107', borderwidth = 0)
submitMove.pack(side = LEFT, expand = True, ipadx = 5, ipady = 5, pady = 5)
submitMove.bind("<Button>", entryText)

quitGame = Button(container3, text = 'Quit', font = buttonfont, fg = '#800080', bg = '#ffc107', borderwidth = 0)
quitGame.pack(side = LEFT, expand = True, ipadx = 5, ipady = 5, pady = 5)
quitGame.bind("<Button>", quit)


frame.pack(expand=True) # Making the Positioning of the Board onto the Center of the window generated.
moveInput.pack(expand = True, side = 'bottom')

container3.pack(expand = True, side = 'bottom', pady = 10, fill = X)
container1.pack(expand = True, side = 'bottom', pady = 10, fill = X)
container2.pack(expand = True, side = 'bottom', pady = 10, fill = X)

root.mainloop()
