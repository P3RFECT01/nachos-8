from renderer import Renderer
from keyboard import Keyboard
from cpu import CPU

import tkinter as tk
import time

class Chip8(tk.Frame):
    def __init__(self):
        super.__init__()
        self.renderer=Renderer(self)
        self.fps=60
        self.cpu=CPU()  

        self.init()

    def init(self):
        self.fpsInterval=1000/self.fps

        self.cpu.load_sprites()
        self.cpu.load_rom('roms/PONG')
        print("Loaded ROM")

    def step(self):
        start_time=time.time()

        self.cpu.cycle()
        self.renderer.render()

        elapsed_time = time.time() - start_time
        remaining_time = max(0, self.fpsInterval - elapsed_time)
        self.after(int(remaining_time * 1000), self.step)