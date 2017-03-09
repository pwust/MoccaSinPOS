# -*- coding: utf-8 -*-
import logging
import tkinter as tk

__project__ = 'MoccaSinPOS'
__author__ = 'pwust'
__created__ = '09.03.2017-09:08'

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)-15s %(name)-5s %(levelname)-8s %(message)s')
#                   levels: CRITICAL 50, ERROR 40, WARNING 30, INFO 20, DEBUG 10, NOTSET 0

logger = logging.getLogger('test-test')


def main():
    root = tk.Tk()

    text1 = tk.Text(root, height=20, width=30)
    photo = tk.PhotoImage(file=r'c:\src\pwust\PycharmProjects\MoccaSinPOS\images\AppLogo_256x256.png')

    text1.insert(tk.END, '\n')
    text1.image_create(tk.END, image=photo)

    text1.pack(side=tk.LEFT)

    text2 = tk.Text(root, height=20, width=50)
    scroll = tk.Scrollbar(root, command=text2.yview)
    text2.configure(yscrollcommand=scroll.set)
    text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
    text2.tag_configure('big', font=('Verdana', 20, 'bold'))
    text2.tag_configure('color', foreground='#476042', font=('Tempus Sans ITC', 12, 'bold'))
    text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(tk.END, 'Not now, maybe later!'))
    text2.insert(tk.END, '\nWilliam Shakespeare\n', 'big')

    quote = """
    To be, or not to be--that is the question:
    Whether 'tis nobler in the mind to suffer
    The slings and arrows of outrageous fortune
    Or to take arms against a sea of troubles
    And by opposing end them. To die, to sleep--
    No more--and by a sleep to say we end
    The heartache, and the thousand natural shocks
    That flesh is heir to. 'Tis a consummation
    Devoutly to be wished.
    """

    text2.insert(tk.END, quote, 'color')
    text2.insert(tk.END, 'follow-up\n', 'follow')
    text2.pack(side=tk.LEFT)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)

    root.mainloop()

if __name__ == '__main__':
    main()

