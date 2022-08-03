import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title('cel7 Art Editor')
        self.root.geometry('550x600')
        self.root.resizable(False, False)
        self.root.configure(background='#505050')
        self.colors = ["#000000", "#F7F7E7", "#F70C67", "#FD9819", "#E7D50D", "#A1E119", "#44BCFF", "#AA8BFF", "#F9ACB0",
                        "#AD3045", "#34956E", "#254469", "#7D8E9A", "#C3BFAF", "#76725E", "#3C3B2E"]
        self.art = [[0 for x in range(7)] for y in range(7)]
        
        self.color = 0
        self.pallet_canvas = tk.Canvas(self.root, bg='#ffffff')
        self.pallet_canvas.place(x=25, y=25, width=400, height=100)

        self.art_canvas = tk.Canvas(self.root, bg='#ffffff')
        self.art_canvas.place(x=65, y=135, width=420, height=420)
        self.art_canvas.bind('<Button-1>', self.draw)

        self.preview_canvas = tk.Canvas(self.root, bg='#ffffff')
        self.preview_canvas.place(x=440, y=25, width=100, height=100)

        self.draw_pallet()
        self.draw_art_canvas()
    
    def translate(self, value, leftMin, leftMax, rightMin, rightMax):
        leftSpan = leftMax - leftMin
        rightSpan = rightMax - rightMin
        valueScaled = float(value - leftMin) / float(leftSpan)
        return rightMin + (valueScaled * rightSpan)

    def draw_pallet(self):
        for y in range(0, 100, 50):
            for x in range(0, 400, 50):
                self.pallet_canvas.create_rectangle(x, y, x+50, y+50, fill=self.colors[int((y/50*8)+x/50)])
        
        ccp = [self.color%8*50, int(self.color/8)*50]
        self.pallet_canvas.create_rectangle(ccp[0], ccp[1], ccp[0]+50, ccp[1]+50, outline='#000000', width=2)

        self.pallet_canvas.bind('<Button-1>', self.set_color)

    def set_color(self, event):
        self.color = int(event.x/50) + int(event.y/50)*8
        self.draw_pallet()

    def draw_art_canvas(self):
        for y in range(7):
            for x in range(7):
                if self.art[y][x] == 1:
                    self.art_canvas.create_rectangle(x*60+1, y*60+1, x*60+60, y*60+60, fill="#191919")
                else:
                    self.art_canvas.create_rectangle(x*60+1, y*60+1, x*60+60, y*60+60, fill="#ffffff")
                self.art_canvas.create_rectangle(x*60, y*60, x*60+60, y*60+60, outline="#000000", width=0.5)
    
    def draw(self, event):
        x = int(event.x/60)
        y = int(event.y/60)
        current = self.art[y][x]
        if current == 0:
            self.art[y][x] = 1
        else:
            self.art[y][x] = 0
        self.draw_art_canvas()
        self.draw_preview()

    def draw_preview(self):
        width = self.translate(1, 0, 7, 0, 100)
        for y in range(7):
            for x in range(7):
                x_ = self.translate(x, 0, 7, 0, 100)
                y_ = self.translate(y, 0, 7, 0, 100)
                if self.art[y][x] == 1:
                    self.preview_canvas.create_rectangle(x_, y_, x_+width, y_+width, fill="#191919")
                else:
                    self.preview_canvas.create_rectangle(x_, y_, x_+width, y_+width, fill="#ffffff")
                self.preview_canvas.create_rectangle(x_, y_, x_+width, y_+width, outline="#ffffff", width=0.5)

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()