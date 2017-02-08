# -*- coding: utf-8 -*-
import tkinter as tk


class Board(tk.Tk):
    def __init__(self, parent=None):
        tk.Tk.__init__(self,parent)
        self.rows = 5
        self.columns = 5
        self.init_board()

    def init_board(self):
        for i in range(self.rows):
            for j in range(self.columns):
                # cmd = lambda: self.button_callback(i, j)
                cmd = lambda y=i, x=j: self.button_callback(x, y)
                b = tk.Button(self, text=str("  "), command=cmd)
                b.grid(row=i, column=j)

    def button_callback(self, row, col):
        print(str(row) + " " + str(col))


if __name__ == '__main__':
    Board().mainloop()
