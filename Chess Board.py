from tkinter import *
import tkinter.font as font

root = Tk()
root.geometry("700x700")
root.title("Grid Example")

frame = Frame(root)

fontsize = font.Font(size=20)

for r in range(8):
    for c in range(8):
        if(r % 2 != 0):
            # For White pawn 
            if(r == 1):
                if(c%2 != 0):
                    Label(frame, text='\u2659',background='#a6a',font=fontsize).grid(row=r,column=c,ipadx=10,ipady=10)
                    c = c + 1
                else:
                    Label(frame, text='\u2659',background='white',font=fontsize).grid(row=r,column=c,ipadx=10,ipady=10)
                    c = c + 1
            else:
                if(c%2 != 0):
                    Label(frame, text=' ',background='#a6a').grid(row=r,column=c,ipadx=20,ipady=20)
                else:
                    Label(frame, text=' ',background='white').grid(row=r,column=c,ipadx=20,ipady=20)
                
        else:
            # For Black Pawn
            if(r == 6):
                if(c%2 != 0):
                    Label(frame, text='\u265F',background='white',font=fontsize).grid(row=r,column=c,ipadx=10,ipady=10)
                    c = c + 1
                else:
                    Label(frame, text='\u265F',background='#a6a',font=fontsize).grid(row=r,column=c,ipadx=10,ipady=10)
                    c = c + 1
            else:
                if(c%2 != 0):
                    Label(frame, text=' ',background='white').grid(row=r,column=c,ipadx=20,ipady=20)
                    
                else:
                    Label(frame, text=' ',background='#a6a').grid(row=r,column=c,ipadx=20,ipady=20)
                    

Wrook = Label(frame, text="\u2656",font=fontsize,background="#a6a").grid(row=0,column=0)
Wrook = Label(frame, text="\u2656",font=fontsize,background="white").grid(row=0,column=7)
Brook = Label(frame, text="\u265C",font=fontsize,background="white").grid(row=7,column=0)
Brook = Label(frame, text="\u265C",font=fontsize,background="#a6a").grid(row=7,column=7)

Wknight = Label(frame, text="\u2658",font=fontsize,background="white").grid(row=0,column=1)
Wknight = Label(frame, text="\u2658",font=fontsize,background="#a6a").grid(row=0,column=6)
Bknight = Label(frame, text="\u265E",font=fontsize,background="#a6a").grid(row=7,column=1)
Bknight = Label(frame, text="\u265E",font=fontsize,background="white").grid(row=7,column=6)

Wbishop = Label(frame, text="\u2657",font=fontsize,background="#a6a").grid(row=0,column=2)
Wbishop = Label(frame, text="\u2657",font=fontsize,background="white").grid(row=0,column=5)
Bbishop = Label(frame, text="\u265D",font=fontsize,background="white").grid(row=7,column=2)
Bbishop = Label(frame, text="\u265D",font=fontsize,background="#a6a").grid(row=7,column=5)

Wqueen = Label(frame, text="\u2655",font=fontsize,background="white").grid(row=0,column=3)
Bqueen = Label(frame, text="\u265B",font=fontsize,background="#a6a").grid(row=7,column=3)

Wking = Label(frame, text="\u2654",font=fontsize,background="#a6a").grid(row=0,column=4)
Bking = Label(frame, text="\u265A",font=fontsize,background="white").grid(row=7,column=4)


frame.pack()
root.mainloop()
