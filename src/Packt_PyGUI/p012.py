# coding=utf-8
import tkinter as tk        # 2
from tkinter import ttk     # 3
win = tk.Tk()


# Modified Button Click function
def clickMe():
    action.configure(text='Hello, ' + name.get())

# Adding a Button
action = ttk.Button(win, text="Click Me!", command=clickMe)

# Position button in 2nd row, 2nd colum (0-based):
action.grid(column=2, row=1)

# Changing our Label
ttk.Label(win, text='Enter a name:').grid(column=0, row=0)


# Adding a text box entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)

# Combo box widget
ttk.Label(win, text="Choose a number:").grid(column=1, row=0)   # 1
number = tk.StringVar()                                         # 2
numberChosen = ttk.Combobox(win, width=12, textvariable=number)  # 3
numberChosen['values'] = (1, 2, 4, 42, 100)                     # 4
numberChosen.grid(column=1, row=1)                              # 5
numberChosen.current(0)                                         # 6

win.title("Python GUI")     # - Add a title
# win.resizable(0, 0)         # - Disable resizing the GUI

nameEntered.focus()         # Place cursor into name Entry

# action.configure(state='disabled')      # Disable the button widget

win.mainloop()              # - Start GUI
