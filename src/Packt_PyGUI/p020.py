# coding=utf-8
import tkinter as tk        # 2
from tkinter import ttk     # 3
from tkinter import scrolledtext

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


# Radiobutton Globals
colors = ["Blue", "Gold", "Red"]    # 1
# other values: http://www.tcl.tk/man/tcl8.5/TkCmd/colors.htm


# Radiobutton Callback      # 4
def radCall():
    radSel = radVar.get()
    if radSel == 0:
        win.configure(background=colors[0])
    elif radSel == 1:
        win.configure(background=colors[1])
    elif radSel == 2:
        win.configure(background=colors[2])

# create three Radiobuttons
radVar = tk.IntVar()

# set to non-existant index value:
radVar.set(99)  # 2

for col in range(3):        # 3
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(win, text=colors[col],
                            variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=5, sticky=tk.W)


# Using a scrolled Text control
scrolW = 30
scrolH = 3

scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)


win.title("Python GUI")     # - Add a title
# win.resizable(0, 0)         # - Disable resizing the GUI

nameEntered.focus()         # Place cursor into name Entry

# action.configure(state='disabled')      # Disable the button widget

win.mainloop()              # - Start GUI
