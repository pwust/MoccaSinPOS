__author__ = 'pwust'

#from tkinter import *
import tkinter as t

class App:

    def __init__(self, master):
        frame = t.Frame(master)
        frame.pack()
        self.button = t.Button(frame,
                         text="QUIT", fg="red",
                         command=frame.quit)
        self.button.pack(side=t.LEFT)
        self.slogan = t.Button(frame,
                         text="Hello",
                         command=self.write_slogan)
        self.slogan.pack(side=t.LEFT)

    def write_slogan(self):
        print ("Tkinter is easy to use!")

root = t.Tk()
app = App(root)
root.mainloop()
