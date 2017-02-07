import tkinter
# from tkinter import *

"""
http://stackoverflow.com/questions/7591294/how-to-create-a-self-resizing-grid-of-buttons-in-tkinter
"""

# Create & Configure root
root = tkinter.Tk()
tkinter.Grid.rowconfigure(root, 0, weight=1)
tkinter.Grid.columnconfigure(root, 0, weight=1)

# Create & Configure frame
frame = tkinter.Frame(root)
frame.grid(row=0, column=0, sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)

# Create a 5x10 (rows x columns) grid of buttons inside the frame
for row_index in range(12):
    tkinter.Grid.rowconfigure(frame, row_index, weight=1)
    for col_index in range(10):
        tkinter.Grid.columnconfigure(frame, col_index, weight=1)
        btn = tkinter.Button(frame)  # create a button inside frame
        btn.grid(row=row_index, column=col_index, sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)

root.mainloop()
