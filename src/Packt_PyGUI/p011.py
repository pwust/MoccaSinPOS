# coding=utf-8
import tkinter as tk        # 2
from tkinter import ttk     # 3
win = tk.Tk()


# Modified Button Click function            # 1
def clickMe():                              # 2
    action.configure(text='Hello, ' + name.get())

# Adding a Button
action = ttk.Button(win, text="Click Me!", command=clickMe)

# Position button in 2nd row, 2nd colum (0-based):
action.grid(column=1, row=1)

# Changing our Label
ttk.Label(win, text='Enter a name:').grid(column=0, row=0)


# Adding a text box entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)


win.title("Python GUI")     # - Add a title
# win.resizable(0, 0)         # - Disable resizing the GUI

nameEntered.focus()         # Place cursor into name Entry

action.configure(state='disabled')      # Disable the button widget

win.mainloop()              # - Start GUI
