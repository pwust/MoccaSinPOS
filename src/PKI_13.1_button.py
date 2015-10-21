__author__ = 'pwust'

import tkinter as tk

def SchreibWas(text):
    print(text)



app = tk.Tk()
btn = tk.Button(app, text = "Klick mich!", command = SchreibWas("hallo... "))




btn.pack()



app.mainloop()

