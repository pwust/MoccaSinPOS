# coding=utf-8
import tkinter as tk        # 2
from tkinter import ttk     # 3
win = tk.Tk()


# Modified Button Click function
def clickMe():
    action.configure(text='Hello, ' + name.get() + ' ' +
                     numberChosen.get())

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
ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
numberChosen['values'] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

# Creating three checkbuttons       # 1
chVarDis = tk.IntVar()              # 2
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled')  # 3
check1.select()                     # 4
check1.grid(column=0, row=4, sticky=tk.W)   # 5

chVarUn = tk.IntVar()              # 6
check2 = tk.Checkbutton(win, text="UnChecked", variable=chVarUn)  # 7
check2.deselect()                     # 8
check2.grid(column=1, row=4, sticky=tk.W)   # 9

chVarEn = tk.IntVar()              # 10
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)  # 11
check3.select()                     # 12
check3.grid(column=2, row=4, sticky=tk.W)   # 13





win.title("Python GUI")     # - Add a title
# win.resizable(0, 0)         # - Disable resizing the GUI

nameEntered.focus()         # Place cursor into name Entry

# action.configure(state='disabled')      # Disable the button widget

win.mainloop()              # - Start GUI
