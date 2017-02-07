import tkinter
import logging

# -*- coding: utf-8 -*-
__author__ = 'pwust'
# Package
# Version

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)-15s %(name)-5s %(levelname)-8s %(message)s')
#                   levels: CRITICAL 50, ERROR 40, WARNING 30, INFO 20, DEBUG 10, NOTSET 0

logger = logging.getLogger('gui-tests')


def quit(form):
    logger.info('quitting!')
    form.destroy()


def changelabels(form):
    form.bu1['text'], form.bu2['text'] = form.bu2['text'], form.bu1['text']
    logger.info('The texts on Buttons 1 and 2 are swapped.')


def creategui():

    gui = tkinter.Tk()

    bu1 = tkinter.Button(gui)
    bu1.configure(text='Button 1', command=changelabels(gui))
    bu1.pack()

    bu2 = tkinter.Button(gui)
    bu2.configure(text='Button 2', command=changelabels(gui))
    bu2.pack()

    bu3 = tkinter.Button(gui)
    bu3.configure(text='B3 - Exit', command=quit(gui))
    bu3.pack()

    return gui


def main():
    logger.info('initializin GUI...')
    mywindow = creategui()
    logger.info('starting GUI.')
    mywindow.mainloop()

if __name__ == '__main__':
    main()