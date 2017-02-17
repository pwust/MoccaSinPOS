# from tkinter import *
import tkinter as tk
from tkinter import ttk

BLUE = '#00f'
RED = '#f00'
GREEN = '#0f0'
WHITE = '#fff'
BLACK = '#000'

p = tk.Tk()

p.geometry('600x350')
# p.configure(bg='#334353')
p.configure(bg=RED)

gui_style = ttk.Style()
# gui_style.configure('My.TButton', foreground='#334353')
gui_style.configure('My.TButton', foreground=GREEN)
# gui_style.configure('My.TFrame', background='#334353')
gui_style.configure('My.TFrame', background=BLUE)

frame = ttk.Frame(p, style='My.TFrame')
frame.grid(column=1, row=1)

ttk.Button(frame, text='test', style='My.TButton').grid(column=0, row=0)
ttk.Button(frame, text='Test 2', style='My.TButton').grid(column=3, row=3)

p.mainloop()
