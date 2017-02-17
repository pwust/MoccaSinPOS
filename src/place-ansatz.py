# coding=utf-8
import tkinter as tk
from tkinter import ttk
import logging

GREEN = '#0f0'
BLUE = '#00f'
RED = '#f00'
WHITE = '#fff'
BLACK = '#f00'


"""
http://stackoverflow.com/questions/7591294/how-to-create-a-self-resizing-grid-of-buttons-in-tkinter
"""

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)-15s %(name)-5s %(levelname)-8s %(message)s')
#                   levels: CRITICAL 50, ERROR 40, WARNING 30, INFO 20, DEBUG 10, NOTSET 0

logger = logging.getLogger('button-grid')


GLOBAL_BG = '#0B660B'


class CashPointTester(tk.Tk):

    logger = logging.getLogger('button-app')

    def __init__(self, parent=None, rows=12, cols=10):
        tk.Tk.__init__(self, parent)
        self.rows = rows
        self.cols = cols
        self.init_app()

    def recalc_sizes(self):
        '''
        Recalculate all relevant sizes for the GUI
        :return:
        '''
        pass

    def init_app(self):
        for x in range(self.cols):
            for y in range(self.rows):
                cmd = lambda x=x, y=y: self.button_callback(x, y)
                b = tk.Button(self, text='{}/{}'.format(x, y), command=cmd)
                b.grid(row=y, column=x)
                if (x == (self.cols - 1)) and (y == (self.rows - 1)):
                    b.configure(text='Exit')

    def button_callback(self, x, y):
        logger.debug('button {:2}/{:2} pressed.'.format(x, y))


class CashPointGridTest1(tk.Tk):

    def __init__(self, parent=None, rows=12, cols=10, numerator=3, denominator=4, center=True):
        tk.Tk.__init__(self, parent)
        self.rows = rows
        self.cols = cols
        self.numerator = numerator
        self.denominator = denominator
        self.center = center
        self.init_app()

    def init_app(self):
        # determine screen size
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        logger.debug('screen size = %sx%s' % (screen_width, screen_height))

        logger.debug('factor for window size used: {}/{}, centering = {}'
                     .format(self.numerator, self.denominator, self.center))

        window_width = self.numerator * screen_width // self.denominator  # 3/4 of the screen size used
        window_height = self.numerator * screen_height // self.denominator  # 3/4 of the screen size used
        logger.debug('window size = %sx%s' % (window_width, window_height))

        if self.center:
            offset_x = (screen_width - window_width) // 2  # centered
            offset_y = (screen_height - window_height) // 2  # centered
        else:
            offset_x = offset_y = 0
        logger.debug('offset      = %sx%s' % (offset_x, offset_y))

        col_width = window_width // self.cols
        row_height = window_height // self.rows
        logger.debug('button size = %sx%s' % (col_width, row_height))

        # self.geometry(newGeometry='{}x{}+{}+{}'.format(window_width, window_height, offest_x, offset_y))

        # move window to center of available screen
        self.geometry(newGeometry='+{}+{}'.format(offset_x, offset_y))

        # self.minsize(width=window_width//2, height=window_height//2)
        # self.maxsize(width=screen_width, height=screen_height)

        # set window to a fixed size:
        self.minsize(width=window_width, height=window_height)
        self.maxsize(width=window_width, height=window_height)
        self.resizable(False, False)

        # make window borderless:
        # self.overrideredirect(1)

        # set background to dark green:
        self.tk_setPalette('#0B660B')

        tk.Grid.rowconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 0, weight=1)

        # Create & Configure frame
        frame = tk.Frame(self)
        frame.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        # Create a 12x10 (default rows x columns) grid of buttons inside the frame
        for col_index in range(self.cols):
            tk.Grid.columnconfigure(frame, col_index, weight=1)
            for row_index in range(self.rows):
                tk.Grid.rowconfigure(frame, row_index, weight=1)
                # Exceptions where not to put a Button:
                if ((row_index != 3) and (row_index != 2)) \
                        or (((row_index == 3) or (row_index == 2))
                            and ((col_index == 0) or (col_index == self.cols - 1))):
                    cmd = lambda x=col_index, y=row_index: self.button_callback(x, y)
                    btn = tk.Button(frame, )
                    btn.configure(text='{}/{}'.format(col_index, row_index))
                    btn.configure(command=cmd)
                    btn.configure(background='#333')
                    btn.configure(width=col_width, height=row_height)
                    # btn.configure(padx=20, pady=4)
                    btn.grid(row=row_index, column=col_index, sticky=tk.N + tk.S + tk.E + tk.W)
                    if (row_index == (self.rows - 1)) and (col_index == (self.cols - 1)):
                        btn.config(text='EXIT')
                lbl = tk.Label(frame, text='I am a label text, and I wonder how long I can get...')
                # lbl = tk.Message(frame, text='I am a label text, and I wonder how long I can get...')
                lbl.configure(anchor=tk.W)
                lbl.configure(background='white')
                lbl.configure(font=('Helvetica', 20, 'bold'))
                lbl.grid(row=2, column=1, columnspan=8, rowspan=2, sticky=tk.N + tk.S + tk.E + tk.W)

    def button_callback(self, x, y):
        logger.debug('button {:2}/{:2} pressed.'.format(x, y))
        if (x == (self.cols - 1)) and (y == (self.rows - 1)):
            logger.info('Pressed "EXIT" -> exiting.')
            self.clicked_exit()

    def clicked_exit(self):
        logger.debug('clicked_exit()')
        self.destroy()


class CashPointGridTest2(tk.Tk):

    def __init__(self, parent=None, rows=12, cols=10, numerator=3, denominator=4, center=True):
        tk.Tk.__init__(self, parent)
        self.rows = rows
        self.cols = cols
        self.numerator = numerator
        self.denominator = denominator
        self.center = center
        self.init_app()

    def init_app(self):
        # determine screen size
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        logger.debug('screen size = %sx%s' % (screen_width, screen_height))

        logger.debug('factor for window size used: {}/{}, centering = {}'
                     .format(self.numerator, self.denominator, self.center))

        window_width = self.numerator * screen_width // self.denominator  # 3/4 of the screen size used
        window_height = self.numerator * screen_height // self.denominator  # 3/4 of the screen size used
        logger.debug('window size = %sx%s' % (window_width, window_height))

        if self.center:
            offset_x = (screen_width - window_width) // 2  # centered
            offset_y = (screen_height - window_height) // 2  # centered
        else:
            offset_x = offset_y = 0
        logger.debug('offset      = %sx%s' % (offset_x, offset_y))

        col_width = window_width // self.cols
        row_height = window_height // self.rows
        logger.debug('button size = %sx%s' % (col_width, row_height))

        # self.geometry(newGeometry='{}x{}+{}+{}'.format(window_width, window_height, offest_x, offset_y))

        # move window to center of available screen
#        self.geometry(newGeometry='{}x{}+{}+{}'.format(window_width, window_height, offset_x, offset_y))

        # self.minsize(width=window_width//2, height=window_height//2)
        # self.maxsize(width=screen_width, height=screen_height)

        # set window to a fixed size:
#        self.minsize(width=window_width, height=window_height)
#        self.maxsize(width=screen_width, height=screen_height)
        # self.maxsize(width=window_width, height=window_height)
        # self.resizable(False, False)


        # make window borderless:
        # self.overrideredirect(1)

        # define styles for ttk
        gui_style = ttk.Style()
        gui_style.configure('My.TButton', foreground=GREEN)
        # gui_style.configure('My.TFrame.blue', background=BLUE)
        # gui_style.configure('My.TFrame.green', background=GREEN)
        # gui_style.configure('My.TFrame.red', background=RED)
        gui_style.configure('My.TFrame', background=GLOBAL_BG)

        # set background to dark green:
        self.tk_setPalette(GLOBAL_BG)

        tk.Grid.rowconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 0, weight=1)

        # Create & Configure frame
        frm_app = ttk.Frame(self, style='My.TFrame')
        # frmApp.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)


        # putting lableframes for POS GUI:
        frm_app.grid(row=0, column=0)

        # TOP AREA: Logo, Menu Button, Receipt Display,

        frm_display = ttk.LabelFrame(frm_app, text=' Top Area ')
        frm_display.grid(column=0, row=0, columnspan=3, sticky=tk.E + tk.W)
        ttk.Button(frm_display, text='tmpBtn').grid(column=0, row=0)

        frm_1st_buttons = ttk.LabelFrame(frm_app, text=' Level 1 ')
        frm_1st_buttons.grid(column=0, row=1, rowspan=2, sticky=tk.N + tk.S)
        for x in range(6):
            for y in range(8):
                ttk.Button(frm_1st_buttons, text="{}/{}".format(x, y)).grid(column=x, row=y)

        frm_2nd_buttons = ttk.LabelFrame(frm_app, text=' Level 2 ')
        frm_2nd_buttons.grid(column=1, row=1)
        for x in range(3):
            for y in range(7):
                ttk.Button(frm_2nd_buttons, text="{}/{}".format(x, y)).grid(column=x, row=y)

        frm_user_display = ttk.LabelFrame(frm_app, text=' User Info ')
        frm_user_display.grid(column=1, row=2, sticky=tk.W + tk.E)
        # ttk.Button(frm_user_display, text='tmpBtn').grid(column=0, row=0)
        ttk.Label(frm_user_display, text='Angemeldeter Bediener:').grid(column=0, row=0, sticky=tk.W+tk.E)
        lbl_active_user = ttk.Label(frm_user_display, text='BEDIENER ???')
        lbl_active_user.grid(column=0, row=1, sticky=tk.W+tk.E)
        lbl_active_user.configure()





        frm_3rd_buttons = ttk.LabelFrame(frm_app, text=' Level 3 ')
        frm_3rd_buttons.grid(column=2, row=1, rowspan=2, sticky=tk.N + tk.S)
        ttk.Button(frm_3rd_buttons, text='tmpBtn').grid(column=0, row=0, columnspan=2)


        # # Create a 12x10 (default rows x columns) grid of buttons inside the frame
        # for col_index in range(self.cols):
        #     tk.Grid.columnconfigure(frmApp, col_index, weight=1)
        #     for row_index in range(self.rows):
        #         tk.Grid.rowconfigure(frmApp, row_index, weight=1)
        #         # Exceptions where not to put a Button:
        #         if ((row_index != 3) and (row_index != 2)) \
        #                 or (((row_index == 3) or (row_index == 2))
        #                     and ((col_index == 0) or (col_index == self.cols - 1))):
        #             cmd = lambda x=col_index, y=row_index: self.button_callback(x, y)
        #             btn = tk.Button(frmApp, )
        #             btn.configure(text='{}/{}'.format(col_index, row_index))
        #             btn.configure(command=cmd)
        #             btn.configure(background='#333')
        #             btn.configure(width=col_width, height=row_height)
        #             # btn.configure(padx=20, pady=4)
        #             btn.grid(row=row_index, column=col_index, sticky=tk.N + tk.S + tk.E + tk.W)
        #             if (row_index == (self.rows - 1)) and (col_index == (self.cols - 1)):
        #                 btn.config(text='EXIT')
        #         lbl = tk.Label(frmApp, text='I am a label text, and I wonder how long I can get...')
        #         # lbl = tk.Message(frmApp, text='I am a label text, and I wonder how long I can get...')
        #         lbl.configure(anchor=tk.W)
        #         lbl.configure(background='white')
        #         lbl.configure(font=('Helvetica', 20, 'bold'))
        #         lbl.grid(row=2, column=1, columnspan=8, rowspan=2, sticky=tk.N + tk.S + tk.E + tk.W)

    def button_callback(self, x, y):
        logger.debug('button {:2}/{:2} pressed.'.format(x, y))
        if (x == (self.cols - 1)) and (y == (self.rows - 1)):
            logger.info('Pressed "EXIT" -> exiting.')
            self.clicked_exit()

    def recalc_sizes(self):
        """
        recalculate button sizes and all frame sizes after a resizing has happened
        :return:
        """
        pass

    def clicked_exit(self):
        logger.debug('clicked_exit()')
        self.destroy()


def main():
    # CashPointTester().mainloop()
    # CashPointGridTest1(numerator=1, denominator=2, center=False).mainloop()
    CashPointGridTest2(numerator=1, denominator=4, center=True, rows=5, cols=5).mainloop()

if __name__ == '__main__':
    main()
