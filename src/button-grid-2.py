# coding=utf-8
import tkinter
import logging
"""
http://stackoverflow.com/questions/7591294/how-to-create-a-self-resizing-grid-of-buttons-in-tkinter
"""

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)-15s %(name)-5s %(levelname)-8s %(message)s')
#                   levels: CRITICAL 50, ERROR 40, WARNING 30, INFO 20, DEBUG 10, NOTSET 0

logger = logging.getLogger('button-grid')


# Create & Configure root
root = tkinter.Tk()

# determine screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

logger.debug('screen size = %sx%s' % (screen_width, screen_height))

window_width = screen_width // 2
window_height = screen_height // 2

logger.debug('window size = %sx%s' % (window_width, window_height))

root.geometry('{}x{}'.format(window_width, window_height))
root.minsize(width=window_width//2, height=window_height//2)

# frame.geometry('{}x{}'.format(window_width, window_height))
# logger.info(frame.winfo_geometry())

tkinter.Grid.rowconfigure(root, 0, weight=1)
tkinter.Grid.columnconfigure(root, 0, weight=1)

# Create & Configure frame
frame = tkinter.Frame(root)
frame.grid(row=0, column=0, sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)

# Create a 12x10 (rows x columns) grid of buttons inside the frame
for row_index in range(12):
    tkinter.Grid.rowconfigure(frame, row_index, weight=1)
    for col_index in range(10):
        tkinter.Grid.columnconfigure(frame, col_index, weight=1)
        btn = tkinter.Button(frame)  # create a button inside frame
        btn.grid(row=row_index, column=col_index, sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)
logger.info(frame.winfo_geometry())

root.mainloop()
