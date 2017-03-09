# -*- coding: utf-8 -*-
import logging
import tkinter as tk
from tkinter import font as tkfont

__project__ = 'MoccaSinPOS'
__author__ = 'pwust'
__created__ = '08.03.2017-11:00'

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)-15s %(name)-5s %(levelname)-8s %(message)s')
#                   levels: CRITICAL 50, ERROR 40, WARNING 30, INFO 20, DEBUG 10, NOTSET 0

logger = logging.getLogger('font-pixel-calc')


def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=728, height=600)  # pixels?
    canvas.pack()
    (x, y) = (5, 5)
    text = 'yellow world'
    fonts = []
    # for (family, size) in [('times', 12), ('times', 24)]:
    #     font = tkfont.Font(family=family, size=size)
    #     (w,h) = (font.measure(text), font.metrics('linespace'))
    #     logger.debug('{} {}:({}, {})'.format(family, size, w, h))
    #     canvas.create_rectangle(x, y, x+w, y+h)
    #     canvas.create_text(x, y, text=text, font=font, anchor='nw')
    #     fonts.append(font)  # save font values from garbage collection
    #     y += h + 5

    my_text = 'n' * 10
    my_other_text = 'm' * 10
    for my_size in range(10, 40, 2):
        my_font = tkfont.Font(family='Arial Narrow', size=my_size)
        for my_actual_text in (my_text, my_other_text):
            # my_font = tkfont.Font(family='Lucida Console', size=my_size)
            my_width = my_font.measure(my_actual_text)
            my_height = my_font.metrics('linespace')
            canvas.create_text(x, y, text='{} ({}pt)'.format(my_actual_text, my_size), font=my_font, anchor='nw')
            logger.debug('size = {}pt, height = {}px, width of "{}" = {}px'.format(my_size, my_height, my_actual_text, my_width))
            y += my_height + 5
            logger.debug('y = {}, window height = {}'.format(y, canvas.winfo_height()))

    tk.mainloop()


if __name__ == '__main__':
    main()

