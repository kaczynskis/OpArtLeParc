from tkinter import *

penSize = 5

class Draw(object):

    def __init__(self):
        self.root = Tk()
        self.c = Canvas(self.root, bg='white', width=600, height=600)
        self.c.grid(row=1, columnspan=5)
        self.setup()
        self.root.mainloop()

    def setup(self):
        self.oldX = None
        self.oldY = None
        self.lineWidth = penSize
        self.c.bind('<B1-Motion>', self.draw)

    def draw(self, event):
        self.lineWidth = 5
        if self.oldX and self.oldY:
            self.c.create_line(self.oldX, self.oldY, event.x, event.y,
                               width=self.lineWidth, fill='red',
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
	    self.c.create_line(self.oldX+5, self.oldY+5, event.x+5, event.y+5,
				width=self.lineWidth, fill='orange',
				capstyle=ROUND, smooth=TRUE, splinesteps=36)
	    self.c.create_line(self.oldX+10, self.oldY+10, event.x+10, event.y+10,
                                width=self.lineWidth, fill='yellow',
                                capstyle=ROUND, smooth=TRUE, splinesteps=36)
	    self.c.create_line(self.oldX+15, self.oldY+15, event.x+15, event.y+15,
                                width=self.lineWidth, fill='green',
                                capstyle=ROUND, smooth=TRUE, splinesteps=36)
            self.c.create_line(self.oldX+20, self.oldY+20, event.x+20, event.y+20,
                                width=self.lineWidth, fill='blue',
                                capstyle=ROUND, smooth=TRUE, splinesteps=36)
            self.c.create_line(self.oldX+25, self.oldY+25, event.x+25, event.y+25,
                                width=self.lineWidth, fill='purple',
                                capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.oldX = event.x
        self.oldY = event.y

if __name__ == '__main__':
    Draw()
