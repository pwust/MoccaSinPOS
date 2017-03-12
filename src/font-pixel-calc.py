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
    my_window_width = 728
    my_window_height = 600
    canvas = tk.Canvas(root, width=my_window_width, height=my_window_height)  # pixels?
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

    my_texts = []
    my_texts.append('n' * 10)
    # my_texts.append('m' * 10)

    for my_size in range(10, 40, 2):
        my_font = tkfont.Font(family='Arial Narrow', size=my_size)
        for my_actual_text in my_texts:
            if y <= my_window_height:
                # my_font = tkfont.Font(family='Lucida Console', size=my_size)
                my_width = my_font.measure(my_actual_text)
                my_height = my_font.metrics('linespace')
                if y + my_height <= my_window_height:
                    canvas.create_text(x, y, text='{} ({}pt)'.format(my_actual_text, my_size), font=my_font, anchor='nw')
                    logger.debug('size = {}pt, height = {}px, width of "{}" = {}px'.format(my_size, my_height, my_actual_text, my_width))
                    y += my_height + 5
                    logger.debug('y = {}, window height = {}'.format(y, my_window_height))


    tk.mainloop()


if __name__ == '__main__':
    main()

