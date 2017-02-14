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

# Creating three checkbuttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)


# Radiobutton Globals       # 1
COLOR1 = "Blue"             # 2
COLOR2 = "Gold"             # 3
COLOR3 = "Red"              # 4
# other values: http://www.tcl.tk/man/tcl8.5/TkCmd/colors.htm


# Radiobutton Callback      # 5
def radCall():              # 6
    radSel = radVar.get()
    if radSel == 1:
        win.configure(background=COLOR1)
    if radSel == 2:
        win.configure(background=COLOR2)
    if radSel == 3:
        win.configure(background=COLOR3)

# create three Radiobuttons         # 7
radVar = tk.IntVar()                # 8
rad1 = tk.Radiobutton(win, text=COLOR1, variable=radVar, value=1, command=radCall)  # 9
rad1.grid(column=0, row=5, sticky=tk.W) # 10

rad2 = tk.Radiobutton(win, text=COLOR2, variable=radVar, value=2, command=radCall)  # 11
rad2.grid(column=1, row=5, sticky=tk.W) # 12

rad3 = tk.Radiobutton(win, text=COLOR3, variable=radVar, value=3, command=radCall)  # 13
rad3.grid(column=2, row=5, sticky=tk.W) # 14




win.title("Python GUI")     # - Add a title
# win.resizable(0, 0)         # - Disable resizing the GUI

nameEntered.focus()         # Place cursor into name Entry

# action.configure(state='disabled')      # Disable the button widget

win.mainloop()              # - Start GUI
