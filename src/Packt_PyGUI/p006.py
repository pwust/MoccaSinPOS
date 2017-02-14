# coding=utf-8
import tkinter as tk        # 2
from tkinter import ttk     # 3
win = tk.Tk()               # - Create instance
# Adding a Label            # 4
ttk.Label(win, text='A Label ------------------------------------------------------|').grid(column=0, row=0)    # 5
# tk.Label(win, text='Another one').grid(column=0, row=1)
win.title("Python GUI")     # - Add a title
# win.resizable(0, 0)         # - Disable resizing the GUI
win.mainloop()              # - Start GUI
