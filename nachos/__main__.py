import tkinter as tk
from .cpu import CPU
from .renderer import Renderer
from .keyboard import Keyboard

def main():

    root = tk.Tk()
    root.title("Nachos-8")

    renderer = Renderer(master=root)
    keyboard = Keyboard(root)

    cpu = CPU(renderer, keyboard)

    def run_emulator():
        #cpu.cycle()
        renderer.render()
        root.after(16, run_emulator)

    run_emulator()

    root.mainloop()

if __name__ == "__main__":
    main()
