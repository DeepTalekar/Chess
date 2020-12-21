from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import socket
from threading import Thread


class Client():
    def __init__(self, name = "Player"):
        self.username = name
        self.host = 'localhost'
        self.port = 8091
        
        self.conn = socket.socket()        
        self.conn.connect((self.host, self.port))

    def main(self):
        chess = ChessGUI(self.username, self.conn)

        # If one tries to close the Window using the Close Button on the window then we will confirm it
        chess.root.protocol('WM_DELETE_WINDOW', chess.quit)
        chess.root.mainloop()


class ChessGUI():
    # def __int__(self, root, name):
    #     self.root = root
    #     self.name = name
    #     self.__init__(self.name)

    def __init__(self, name, connection = socket.socket()):
        # super().__init__(name)
        self.root = Tk()
        self.name = name
        self.conn = connection
        self.reciever = Thread(target=self.Reciever)
        self.reciever.start()
        self.root.state('zoomed')
        self.root.title("{} | Chess".format(self.name))

        # self.client = Client()

        self.board = [
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

        self.myFont = font.Font(family="Courier",size=20,weight="bold")
        self.labelfont = font.Font(family = "Arial", size = 15, weight = "bold")
        self.fontsize = font.Font(size = 20)     # Just for Some good Visuals :))
        self.buttonfont = font.Font(family = "Courier", size = 15, weight = "bold")

        self.frame = Frame(self.root)
        self.moveInput = Frame(self.root)

        self.container1 = Frame(self.moveInput)
        self.container2 = Frame(self.moveInput)
        self.container3 = Frame(self.moveInput)

        self.Create_Board()

        Label(self.moveInput, text = "Enter the Row and Column Below to Make a Move", font = self.myFont, fg = '#4169e1').pack(side = TOP, expand = True, pady = 10)

        # For Row Input 
        Label(self.container1, text = "Initial Row Index:", font = self.labelfont, fg = '#007bff').pack(side = 'left', expand = True, padx = 10, pady = 20)
        self.initialrowInput = Entry(self.container1, font = self.labelfont, fg = '#28a745', justify = 'center')
        self.initialrowInput.pack(side = LEFT, expand = True, padx = 10, pady = 20)

        self.finalrowInput = Entry(self.container1, font = self.labelfont, fg = '#28a745', justify = 'center')
        self.finalrowInput.pack(side = RIGHT, expand = True, padx = 10, pady = 20)
        Label(self.container1, text = "Final Row Index:", font = self.labelfont, fg = '#007bff').pack(side = RIGHT, expand = True, padx = 10, pady = 10)

        # For Column Input
        Label(self.container2, text = "Initial Column Letter:", font = self.labelfont, fg = '#007bff').pack(side = 'left', expand = True, padx = 10, pady = 10)
        self.initialcolumnInput = Entry(self.container2, font = self.labelfont, fg = '#28a745', justify = 'center')
        self.initialcolumnInput.pack(side = LEFT, expand = True, padx = 10, pady = 10)

        self.finalcolumnInput = Entry(self.container2, font = self.labelfont, fg = '#28a745', justify = 'center')
        self.finalcolumnInput.pack(side = RIGHT, expand = True, padx = 10, pady = 10)
        Label(self.container2, text = "Final Column Letter:", font = self.labelfont, fg = '#007bff').pack(side = RIGHT, expand = True, padx = 10, pady = 10)

        # Submit Move via Button
        self.submitMove = Button(self.container3, text = 'Submit', font = self.buttonfont, fg = '#800080', bg = '#ffc107', borderwidth = 0)
        self.submitMove.pack(side = LEFT, expand = True, ipadx = 5, ipady = 5, pady = 5)
        self.submitMove.bind("<Button>", self.entryText)

        # Reset Board via Button
        self.resetBoard = Button(self.container3, text = 'Reset Board', font = self.buttonfont, fg = '#800080', bg = '#ffc107', borderwidth = 0)
        self.resetBoard.pack(side = LEFT, expand = True, ipadx = 5, ipady = 5, pady = 5)
        self.resetBoard.bind("<Button>", self.reset)

        # Quit the Game via Button
        self.quitGame = Button(self.container3, text = 'Quit', font = self.buttonfont, fg = '#800080', bg = '#ffc107', borderwidth = 0)
        self.quitGame.pack(side = LEFT, expand = True, ipadx = 5, ipady = 5, pady = 5)
        self.quitGame.bind("<Button>", self.quit)

        self.frame.pack(expand=True) # Making the Positioning of the Board onto the Center of the window generated.
        self.moveInput.pack(expand = True, side = 'bottom')

        self.container3.pack(expand = True, side = 'bottom', pady = 10, fill = X)
        self.container1.pack(expand = True, side = 'bottom', pady = 10, fill = X)
        self.container2.pack(expand = True, side = 'bottom', pady = 10, fill = X)

       




    # Logic behind Creating the Chess Board using the above list
    def Create_Board(self):
        self.temp = self.label = Label(self.frame)
        r = c = 0
        for r in range(9):
            for c in range(9):
                if r > 0 and c > 0:
                    self.temp = Label(self.frame, text = self.board[r][c], font = self.fontsize)
                    self.temp.grid(row = r,column = c,ipadx = 30,ipady = 20)
                    if r % 2 != 0:
                        if c % 2 != 0:
                            self.temp.config(bg = '#a6a')
                        else:
                            self.temp.config(bg = 'white')
                    else:
                        if c % 2 != 0:
                            self.temp.config(bg = 'white')
                        else:
                            self.temp.config(bg = '#a6a')
                else:
                    self.temp = Label(self.frame, text = self.board[r][c], font = self.fontsize)
                    self.temp.grid(row = r,column = c,ipadx = 25,ipady = 20) 


    def sendMoveDetails(self, movedata):
        print("Inside sendMoveDetails!!")
        d1 = dict(movedata)
        print("The Dictionary that we catched -->", d1)
        separator = ', '
        s1 = str(d1)
        print("The string of the above list is --> ", s1)

        s1 = s1.encode()
        self.conn.send(s1)

    def makeMove(self, move):
        self.inittemp = Label(self.frame)
        self.finaltemp = Label(self.frame)
        self.displayMove = eval(move)
        print("||Just going to make a move on the board||")
        print("The Dict in makeMove Function: ", self.displayMove)

        # Finding the Index of the Initial and Final Column on the Board
        self.initcolumn = self.board[0].index(self.displayMove['ic'])
        self.finalcolumn = self.board[0].index(self.displayMove['fc'])
        print("The Initial column: ", self.initcolumn)
        print("The Final column: ", self.finalcolumn)

        # Finding the Index of the Initial and Final Row on the Board
        self.initrow = self.findindexOf(self.displayMove['ir'])
        self.finalrow = self.findindexOf(self.displayMove['fr'])
        print("The Initial row: ", self.initrow)
        print("The Final row: ", self.finalrow)

        self.initElement = self.board[self.initrow][self.initcolumn]
        self.finalElement = self.board[self.finalrow][self.finalcolumn]
        print("The Initial Position consited of: ", self.initElement)
        print("The Final Position consited of: ", self.finalElement)

        # If there is an piece in place of final element we directly replace it with ' '
        if self.finalElement == ' ':
            pass
        else: 
            self.finalElement = ' '
            pass
        # Since we can't access the Background color and text on the specific cell of the grid 
        # We have to re-render the Whole board
        # Also the Board List is been modified
        self.board[self.initrow][self.initcolumn] = self.finalElement
        self.board[self.finalrow][self.finalcolumn] = self.initElement

        self.Create_Board()
    
    def entryText(self,event):

        initcolumn = self.initialcolumnInput.get()
        initcolumn = initcolumn.lower()
        initrow = self.initialrowInput.get()
        initrow = int(initrow.lower())
        finalrow = self.finalrowInput.get()
        finalrow = int(finalrow.lower())
        finalcolumn = self.finalcolumnInput.get()
        finalcolumn = finalcolumn.lower()
        print("Message from the Init column textfiled --> ", initcolumn)
        print("Message from the Init row textfiled --> ", initrow)
        print("Message from the Final column textfiled --> ", finalcolumn)
        print("Message from the Final row textfiled --> ", finalrow)

        self.moveDict = { 'ic' : initcolumn, 'ir' : initrow, 'fc' : finalcolumn, 'fr' : finalrow }

        

        self.sendMoveDetails(self.moveDict)

        self.initialcolumnInput.delete(0,END)
        self.initialrowInput.delete(0,END)
        self.finalcolumnInput.delete(0,END)
        self.finalrowInput.delete(0, END)

    
    def findindexOf(self, row):
        for i in range(len(self.board)):
            if(row == self.board[i][0]):
                return i
    
    def reset(self, event):
        if messagebox.askquestion("Confirm - Reset Board","Do you want to Reset the Current Board ?", icon = 'warning'):
            resetMessage = "Reset_Board"
            self.conn.send(resetMessage.encode())

    def reset_board(self):
        self.board = [
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

        self.Create_Board()
        print("Board Reset Successful!")

    def quit(self, event = None):
        if messagebox.askyesno('Confirm - Want to Quit the Game ?', 'Do You really want to Quit the Game ?'):
            self.conn.send("q".encode())
            print("Waiting for The Reciever Thread")
            print(self.reciever)
            self.reciever.join()    # To make this thread end first and then Quit the Game
            print("Reciever Thread Terminated Succesfully")
            self.root.destroy()
            self.conn.close()
            

    def Reciever(self):
        self.move = self.conn.recv(1024)
        self.move = self.move.decode()
        if self.move != "You just quitted the Game":
            self.makeMove(self.move)
        while self.move != "You just quitted the Game":
            print("Server Echoing {}".format(self.move))
            self.move = self.conn.recv(1024)
            self.move = self.move.decode()
            if self.move != "You just quitted the Game":
                if self.move != "Reset_Board":
                    self.makeMove(self.move)
                else:
                    self.reset_board()
        self.conn.close()
        self.root.quit()


if __name__ == "__main__":
    start = Client()
    start.main()
