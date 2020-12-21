# List of Fonts in Tkinter
# https://www.delftstack.com/howto/python-tkinter/how-to-set-font-of-tkinter-text-widget/
import runpy
import glob
from New_Chess_Client2 import Client
from PIL import Image as pilImage, ImageTk as pilImageTk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter.font as font

class Slideshow():
    def __init__(self, frame):
        self.master = frame
        self.outerFrame = Frame(self.master)
        self.frame = Frame(self.outerFrame)

        self.count = 0
        self.imgs = Label(self.frame)
        self.imgs.pack()

        self.outerFrame.pack(expand = True)
        self.frame.pack(expand = True)
        self.display()
    
    def display(self):
        self.fileList = []

        for filename in glob.glob(r'E:\\Deep\\Python\\Chess\\Chess Board Images\\SlideShow\\*'):
            self.temp = filename
            self.fileList.append(self.temp)

        if (self.count == len(self.fileList) - 1):
            self.count = 0
        else:
            self.count += 1


        self.file = self.fileList[self.count]
        # To maintain the Orginial Aspect of the image
        self.load = pilImage.open(self.file)
        # Since Size returns a Tuple with Width and Height
        self.imageWidth = self.load.size[0]            
        self.imageHeight = self.load.size[1] 

        # Now calculating the Original Aspect
        self.orgAspect = self.imageWidth / self.imageHeight
        self.calculateWidth = int(self.orgAspect * 650)
        self.calculateHeight = int(self.orgAspect * 500)

        self.load2 = self.load.resize((self.calculateWidth, self.calculateHeight))

        self.renderImage = pilImageTk.PhotoImage(self.load2)
        self.imgs.config(image = self.renderImage)
        
        frame.after(2000, self.display)


def play(event = None):
    global nameText, root
    username = nameText.get()
    if username == "":
        messagebox.showerror("Cannot Proceed Futher","Please Enter Your Name to Proceed")
    else:
        if messagebox.askquestion("Confirm Your Name", "Do you want to Proceed with the this {} Name to the Game ?".format(username)):
            root.destroy()
            root.quit()
            print("Destroying Dashboard")
            startGame = Client(username)
            startGame.main()

def Quit(event = None):
    global nameText
    if nameText.get() != "":
        if messagebox.askyesno("Confirm Status", "{} do you want to Quit ?".format(nameText.get())):
            root.destroy()
    else:
        if messagebox.askyesno("Confirm Status", "Do you want to Quit ?"):
            root.destroy()
    

root = Tk()
root.title("The Ultimate Chess Game")
root.state('zoomed')
root.configure(bg = '#fff')
root.iconbitmap(default = 'Chess Board Images\Dashboard.ico')


headingFont = font.Font(family = 'Impact', size = 30)
labelFont = font.Font(family = 'Verdana', size = 20)



frame = Frame(root, bg = 'white')

credentials = Frame(frame, borderwidth = 1, bg = '#fff')
inputCredentials = Frame(credentials, borderwidth = 1, bg = '#fff')
imageside = Frame(frame,borderwidth = 1, bg = '#fff')

quote = Label(credentials, text = "\"Strategy requires Thought, Tactics require Observation\"", font = headingFont, bg = '#fff')
quote.pack(side = TOP,expand = True, fill = Y)

name = Label(inputCredentials, text = "Please Enter Your Name", font = labelFont, bg = '#fff')
name.pack(side = TOP, expand = True, padx = 10, pady = 20)

nameText = Entry(inputCredentials, font = labelFont, bg = '#fff')
nameText.pack(side = BOTTOM, expand = True, padx = 10)

profileImage = PhotoImage(file = 'Chess Board Images\Dashboard2.png')
profile = Label(credentials, image = profileImage, bg = '#fff')
profile.pack(side = TOP, expand = True, pady = 150)

playimage = PhotoImage(file = 'Chess Board Images\Play.gif')
playButton = Button(credentials, image = playimage, borderwidth = 0, bg = '#fff', activebackground = '#fff')
playButton.pack(side = BOTTOM, expand = True, pady = 10)
playButton.bind("<Button>", play)


slideshow = Slideshow(imageside)

frame.pack(expand = True)
credentials.pack(side = LEFT, expand = True, fill = X)
inputCredentials.pack(side = BOTTOM, expand = True, fill = X, pady = 10)
imageside.pack(side = RIGHT, expand = True, fill = Y, ipadx = 150)

root.protocol('WM_DELETE_WINDOW', Quit)
root.mainloop()
