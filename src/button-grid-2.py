# coding=utf-8
import tkinter as tk
import tkinter.ttk as ttk
import logging
"""
http://stackoverflow.com/questions/7591294/how-to-create-a-self-resizing-grid-of-buttons-in-tkinter
"""

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)-15s %(name)-5s %(levelname)-8s %(message)s')
#                   levels: CRITICAL 50, ERROR 40, WARNING 30, INFO 20, DEBUG 10, NOTSET 0

logger = logging.getLogger('button-grid')


class App(tk.Tk):
    def __init__(self, parent=None):
        tk.Tk.__init__(self, parent)
        self.rows = 12
        self.cols = 10
        self.init_app()
        logger = logging.getLogger('button-app')

    def init_app(self):
        for x in range(self.cols):
            for y in range(self.rows):
                cmd = lambda x=x, y=y: self.button_callback(x, y)
                b = tk.Button(self, text='{}/{}'.format(x, y), command=cmd)
                b.grid(row=y, column=x)
                if (x == (self.cols - 1)) and (y == (self.rows - 1)):
                    b.configure(text='Exit')

    def button_callback(self, x, y):
        logger.debug('button {}/{} pressed.'.format(x, y))



def clicked(x, y):
    logger.debug('clicked on button {}/{}'.format(x, y))
    if (x == (col_count - 1)) and (y == (row_count - 1)):
        logger.info('exiting.')
        root.destroy()


# Create & Configure root
root = tk.Tk()

# determine screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
logger.debug('screen size = %sx%s' % (screen_width, screen_height))

window_width = 7 * screen_width // 8    # 3/4 of the screen size used
window_height = 7 * screen_height // 8  # 3/4 of the screen size used
logger.debug('window size = %sx%s' % (window_width, window_height))

offest_x = (screen_width - window_width) // 2  # centered
offset_y = (screen_height - window_height) // 2  # centered
logger.debug('offset      = %sx%s' % (offest_x, offset_y))

col_count = 10
row_count = 12

col_width = window_width // col_count
row_height = window_height // row_count
logger.debug('button size = %sx%s' % (col_width, row_height))

# logger.debug('window size = %sx%s (min=half, max=screen)' % (window_width, window_height))

# root.geometry(newGeometry='{}x{}+{}+{}'.format(window_width, window_height, offest_x, offset_y))
root.geometry(newGeometry='+{}+{}'.format(offest_x, offset_y))

# root.minsize(width=window_width//2, height=window_height//2)
# root.maxsize(width=screen_width, height=screen_height)
root.minsize(width=window_width, height=window_height)
root.maxsize(width=window_width, height=window_height)

# make window borderless:
root.overrideredirect(1)


# frame.geometry('{}x{}'.format(window_width, window_height))
# logger.info(frame.winfo_geometry())

tk.Grid.rowconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 0, weight=1)

# Create & Configure frame
frame = tk.Frame(root)
frame.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

# Create a 12x10 (rows x columns) grid of buttons inside the frame
for row_index in range(row_count):
    tk.Grid.rowconfigure(frame, row_index, weight=1)
    for col_index in range(col_count):
        tk.Grid.columnconfigure(frame, col_index, weight=1)
        if ((row_index != 3) and (row_index != 2)) or \
                (((row_index == 3) or (row_index == 2)) and ((col_index == 0) or (col_index == 9))):
            btn = tk.Button(frame,)  # create a button inside frame
            btn.grid(row=row_index, column=col_index, sticky=tk.N+tk.S+tk.E+tk.W)
            btn.config(text="({}/{})".format(col_index, row_index))
            btn.config(width=col_width, height=row_height)
            btn.config(command=lambda y=row_index, x=col_index: clicked(x, y))
            if (row_index == (row_count - 1)) and (col_index == (col_count - 1)):
                btn.config(text='EXIT')


root.mainloop()

App().mainloop()