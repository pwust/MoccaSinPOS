# coding=utf-8
import tkinter as tk        # 2
from tkinter import ttk     # 3
win = tk.Tk()               # - Create instance
# Modify adding a Label                     # 1
aLabel = ttk.Label(win, text='A Label ')    # 2
aLabel.grid(column=0, row=0)                # 3


# Button click event callback function      # 4
def clickMe():                              # 5
    action.configure(text="** I have been clicked! **")
    aLabel.configure(foreground='red')

# Adding a Button                           # 6
action = ttk.Button(win, text="Click Me!", command=clickMe)     # 7
action.grid(column=1, row=0)                # 8


# tk.Label(win, text='Another one').grid(column=0, row=1)  # - tk label with grid
win.title("Python GUI")     # - Add a title
# win.resizable(0, 0)         # - Disable resizing the GUI
win.mainloop()              # - Start GUI
