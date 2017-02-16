# coding=utf-8

import tkinter as tk
from tkinter import ttk

win=tk.Tk()
win.title("Python GUI")

tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)


tabControl.add(tab1, text="Tab 1")
tabControl.add(tab2, text="Tab 2")
tabControl.pack(expand=1, fill="both")

monty = ttk.LabelFrame(tab1, text=' Monty Python ')
monty.grid(column=0, row=0, padx=8, pady=4)
ttk.Label(monty, text="Enter a name:").grid(column=0, row=0, sticky=tk.W    )


win.mainloop()
