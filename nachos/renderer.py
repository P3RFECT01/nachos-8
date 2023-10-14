import tkinter as tk
import math

class Renderer(tk.Canvas):
    def __init__(self,master, scale=20,col=64, row=32):
        super().__init__(master)
        self.master=master
        self.col = col
        self.row = row
        self.scale = scale
        self.display = [0] * (col * row)

    def setPixel(self, x, y):
        if x >= self.col:
            x -= self.col
        elif x < 0:
            x += self.col

        if y >= self.row:
            y -= self.row
        elif y < 0:
            y += self.row

        pixelLoc = x + y * self.col
        self.display[pixelLoc] ^= 1
        return not self.display[pixelLoc]

    def clear(self):
        self.display = [0] * (self.col * self.row)

    def render(self):
        self.delete("all")  # Clear the canvas
        for y in range(self.row):
            for x in range(self.col):
                if self.display[x + y * self.col]:
                    x0 = x * self.scale
                    y0 = y * self.scale
                    x1 = x0 + self.scale
                    y1 = y0 + self.scale
                    self.create_rectangle(x0, y0, x1, y1, fill="#FFFFFF")

    def testRenderer(self):
        self.setPixel(0, 0)
        self.setPixel(5, 2)
        self.render()
