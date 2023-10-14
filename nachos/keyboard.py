class Keyboard():
    def __init__(self,master):

        self.KEYMAP={
            '1': 0x1, # 1-Key
            '2': 0x2, # 2-Key
            '3': 0x3, # 3-Key
            '4': 0xc, # 4-Key
            'q': 0x4, # Q-Key
            'w': 0x5, # W-Key
            'e': 0x6, # E-Key
            'r': 0xD, # R-Key
            'a': 0x7, # A-Key
            's': 0x8, # S-Key
            'd': 0x9, # D-Key
            'f': 0xE, # F-Key
            'z': 0xA, # Z-Key
            'x': 0x0, # X-Key
            'c': 0xB, # C-Key
            'v': 0xF  # V-Key
        }

        self.keysPressed=[]

        self.onNextKeyPress=None


        master.bind("<KeyPress>", self.key_down)
        master.bind("<KeyRelease>", self.key_up)

    def key_down(self, event):
        key = event.keysym.lower()
        keycode = self.KEYMAP.get(key, None)
        if keycode is not None:
            if keycode not in self.keysPressed:
                self.keysPressed.append(keycode)
            if self.onNextKeyPress is not None:
                self.onNextKeyPress(keycode)

    def key_up(self, event):
        key = event.keysym.lower()
        keycode = self.KEYMAP.get(key, None)
        if keycode is not None and keycode in self.keysPressed:
            self.keysPressed.remove(keycode)