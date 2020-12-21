from PIL import Image, ImageTk
import tkinter as tk
import random
import glob

class Slideshow():
    def __init__(self, root):
        self.root = root
        self.root.title("Slideshow")
        self.root.state('zoomed')

        self.frame = tk.Frame(root, bg = '#000')
        # self.frame.place(relheight = 0.85, relwidth = 0.85, relx = 0.05,rely = 0.05)
        self.frame.pack()

        self.count = 0
        self.img = tk.Label(self.frame)
        self.img.pack()
        self.color()
        self.pic()
    
    def color(self):
        self.colors = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
          'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
          'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
          'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
          'light slate gray', 'gray', 'light gray', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
          'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
          'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
          'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
          'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
          'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
          'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
          'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
          'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
          'indian red', 'saddle brown', 'sandy brown']

        randomColor = random.choice(self.colors)
        self.root.configure(bg = randomColor)
        root.after(1000, self.color)
        
    def pic(self):
        
        self.fileList = []

        for name in glob.glob(r'E:\\Deep\\Python\\Chess\\Chess Board Images\\SlideShow\\*'):
            self.val = name
            self.fileList.append(self.val)
        
        if self.count == len(self.fileList) - 1:
            self.count = 0
        else:
            self.count += 1

        self.file = self.fileList[self.count]

        # To keep the Original Aspect of the Image
        self.load = Image.open(self.file)
        self.picWidth = self.load.size[0]
        self.picHeight = self.load.size[1]

        self.orgAspect = self.picWidth / self.picHeight

        self.calWidth = int(self.orgAspect * 800)

        self.load2 = self.load.resize((self.calWidth, 800))

        self.render = ImageTk.PhotoImage(self.load2)
        self.img.config(image = self.render)
        self.img.image = self.render
        root.after(1000, self.pic)

root = tk.Tk()
slideshow = Slideshow(root)
root.mainloop()
