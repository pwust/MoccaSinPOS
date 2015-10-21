__author__ = 'pwust'

import tkinter as t
import random

tk = t.Tk()
canvas = t.Canvas(tk, width=400, height=400)
canvas.pack()

def random_rectangle(width, height):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    colors = [random.randint(0,15),random.randint(0,15),random.randint(0,15)]
    colorcode = '#' + ''.join('{:1x}'.format(a) for a in colors)
    print("%3s %3s %3s %3s %4s" % (x1, y1, x2, y2, colorcode))
    canvas.create_rectangle(x1, y1, x2, y2, outline=colorcode)

for x in range(0,100):
    random_rectangle(400, 400)

tk.mainloop()