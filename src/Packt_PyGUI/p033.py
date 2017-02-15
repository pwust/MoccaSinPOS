# coding=utf-8
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


# Modified Button Click function
def clickMe():
    action.configure(text='Hello, ' + name.get() + ' ' +
                          numberChosen.get())

win = tk.Tk()

win.title("Python GUI")     # - Add a title

# win.resizable(0, 0)         # - Disable resizing the GUI


# We are creating a container frame to hold all other widgets   # 1
monty = ttk.LabelFrame(win, text=' Monty Python ')
monty.grid(column=0, row=0)



# Adding a Button
action = ttk.Button(monty, text="Click Me!", command=clickMe)

# Position button in 2nd row, 2nd colum (0-based):
action.grid(column=2, row=1)

# Changing our Label
ttk.Label(monty, text='Enter a name:').grid(column=0, row=0, sticky=tk.W)


# Adding a text box entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(monty, width=12, textvariable=name)
nameEntered.grid(column=0, row=1, sticky=tk.W)

# Combo box widget
ttk.Label(monty, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(monty, width=12, textvariable=number, state='readonly')
numberChosen['values'] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

# Creating three checkbuttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(monty, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(monty, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(monty, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)


# Radiobutton Globals
colors = ["Blue", "Gold", "Red"]
# other values: http://www.tcl.tk/man/tcl8.5/TkCmd/colors.htm


# Radiobutton Callback
def radCall():
    radSel = radVar.get()
    win.configure(background=colors[radSel])
    # if radSel == 0:
    #     win.configure(background=colors[0])
    # elif radSel == 1:
    #     win.configure(background=colors[1])
    # elif radSel == 2:
    #     win.configure(background=colors[2])

# create three Radiobuttons
radVar = tk.IntVar()

# set to non-existant index value:
radVar.set(99)

for col in range(3):
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(monty, text=colors[col],
                            variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W)


# Using a scrolled Text control
scrolW = 30
scrolH = 3

scr = scrolledtext.ScrolledText(monty, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, columnspan=3, row=5, sticky=tk.EW)



# action.configure(state='disabled')      # Disable the button widget


# Create a container to hold labels
labelsFrame = ttk.LabelFrame(monty, text=' Labels in a Frame ')
labelsFrame.grid(column=0, row=7)

# Place labels into the container element
ttk.Label(labelsFrame, text="Label1").grid(column=0, row=0)
ttk.Label(labelsFrame, text="Label2").grid(column=0, row=1)
ttk.Label(labelsFrame, text="Label3").grid(column=0, row=2)


# add space aroung the labels in the labelframe:
for child in labelsFrame.winfo_children():
    child.grid_configure(padx=8, pady=4)


nameEntered.focus()         # Place cursor into name Entry

win.mainloop()              # - Start GUI
