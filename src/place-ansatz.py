# coding=utf-8
import tkinter as tk
from tkinter import ttk
import logging

GREEN = '#0f0'
BLUE = '#00f'
RED = '#f00'
WHITE = '#fff'
BLACK = '#000'


"""
http://stackoverflow.com/questions/7591294/how-to-create-a-self-resizing-grid-of-buttons-in-tkinter
"""

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)-15s %(name)-5s %(levelname)-8s %(message)s')
#                   levels: CRITICAL 50, ERROR 40, WARNING 30, INFO 20, DEBUG 10, NOTSET 0

logger = logging.getLogger('button-grid')


GLOBAL_BG = '#0B660B'


class CashPointTest(tk.Tk):

    def __init__(self, parent=None, rows=12, cols=10, numerator=3, denominator=4, center=True):
        tk.Tk.__init__(self, parent)
        self.rows = rows
        self.cols = cols
        self.numerator = numerator
        self.denominator = denominator
        self.center = center
        self.window_width = 0
        self.window_height = 0
        self.btn_width = 0
        self.btn_height = 0
        self.btn_1st_grid_width = 0
        self.btn_1st_grid_height = 0
        self.btn_2nd_grid_width = 0
        self.btn_2nd_grid_height = 0
        self.btn_3rd_grid_width = 0
        self.btn_3rd_grid_height = 0
        self.userinfo_grid_width = 0
        self.userinfo_grid_height = 0
        self.current_item_grid_width = 0
        self.current_item_grid_height = 0
        self.top_area_width = 0
        self.top_area_height = 0
        self.recalc_sizes()
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

        self.geometry(newGeometry='{}x{}+{}+{}'.format(window_width, window_height, offset_x, offset_y))

        # move window to center of available screen
        #        self.geometry(newGeometry='{}x{}+{}+{}'.format(window_width, window_height, offset_x, offset_y))

        self.minsize(width=window_width // 2, height=window_height // 2)
        self.maxsize(width=screen_width, height=screen_height)

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
        gui_style.configure('Userinfo.TLabel', foreground=WHITE, background=BLACK, font='Arial')
        # gui_style.configure()
        # gui_style.configure('TButton', font='Courier New')
        gui_style.configure('TLabelframe', background=GLOBAL_BG)
        gui_style.configure('TFrame', background=GLOBAL_BG)
        # logger.debug('Style for TLabelframe -> font: {}'.format(ttk.Style().lookup("TLabelframe", "font")))
        # logger.debug('Style for TButton -> width: {}'.format(ttk.Style().lookup("TButton", "width")))

        # logger.debug('Themes available: {}'.format(gui_style.theme_names()))
        # logger.debug('Elements available: {}'.format(gui_style.element_names()))

        # set background to dark green:
        self.tk_setPalette(GLOBAL_BG)

        tk.Grid.rowconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 0, weight=1)

        # Create & Configure frame
        frm_app = ttk.Frame(self, style='My.TFrame')

        # putting lableframes for POS GUI:
        frm_app.grid(row=0, column=0, sticky='nesw')
        # frm_app.grid_propagate(0)
        # logger.debug('frm_app: {}'.format(frm_app.grid_info()))

        # TOP AREA: Logo, Menu Button, Receipt Display,

        frm_display = ttk.LabelFrame(frm_app, text=' Top Area ')
        frm_display.grid(column=0, row=0, columnspan=3, rowspan=1, sticky='ew')
        # frm_display.grid_propagate(0)
        # logger.debug('frm_display: {}'.format(frm_display.grid_info()))

        logger.debug('frm_display is of class {}'.format(frm_display.winfo_class()))
        ttk.Button(frm_display, text='EXIT', command=self.clicked_exit).grid(column=0, row=0)

        frm_1st_buttons = ttk.LabelFrame(frm_app, text=' Level 1 ')
        frm_1st_buttons.grid(column=0, row=1, rowspan=2, sticky='ns')
        # logger.debug('frm_1st_buttons: {}'.format(frm_1st_buttons.grid_info()))
        for x in range(6):
            for y in range(8):
                ttk.Button(frm_1st_buttons, text="{}/{}".format(x, y)).grid(column=x, row=y)

        frm_2nd_buttons = ttk.LabelFrame(frm_app, text=' Level 2 ')
        frm_2nd_buttons.grid(column=1, row=1)
        # logger.debug('frm_2nd_buttons: {}'.format(frm_2nd_buttons.grid_info()))
        for x in range(3):
            for y in range(7):
                ttk.Button(frm_2nd_buttons, text="{}/{}".format(x, y)).grid(column=x, row=y)

        frm_user_display = ttk.LabelFrame(frm_app, text=' User Info ')
        frm_user_display.grid(column=1, row=2, sticky='ew')
        # frm_user_display.grid_propagate(0)
        # logger.debug('frm_user_display: {}'.format(frm_user_display.grid_info()))
        # ttk.Button(frm_user_display, text='tmpBtn').grid(column=0, row=0)
        ttk.Label(frm_user_display, text='Angemeldeter Bediener:').grid(column=0, row=0, sticky='ew')
        lbl_active_user = ttk.Label(frm_user_display, text='BEDIENER - ??')
        lbl_active_user.grid(column=0, row=1, sticky='ew')
        lbl_active_user.configure(style='Userinfo.TLabel')

        frm_3rd_buttons = ttk.LabelFrame(frm_app, text=' Level 3 ')
        frm_3rd_buttons.grid(column=2, row=1, rowspan=2, sticky='ns')
        # logger.debug('frm_3rd_buttons: {}'.format(frm_3rd_buttons.grid_info()))
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
        global layout figures:
        - total window width = 100%
        - each button width in 9 columns = 9% (81% total width)
        - rightmost column = 19%, button width = 13%, right justified
        - total height = 100% (560px)
        - button area height = 72% (410px)
        - each button height = 9%
        - current item line = 7%
        - top are with receipt, logo, etc = 19% (113px)
        :return:
        """
        self.window_width = self.winfo_screenmmwidth()
        self.window_height = self.winfo_screenheight()
        self.btn_width = .09 * self.window_width
        self.btn_height = .09 * self.window_height
        self.btn_1st_grid_width = 6 * self.btn_width
        self.btn_1st_grid_height = 8 * self.btn_height
        self.btn_2nd_grid_width = 3 * self.btn_width
        self.btn_2nd_grid_height = 7 * self.btn_height
        self.btn_3rd_grid_width = self.window_width - self.btn_1st_grid_width - self.btn_2nd_grid_width
        self.btn_3rd_grid_height = self.btn_1st_grid_height
        self.userinfo_grid_width = self.btn_2nd_grid_width
        self.userinfo_grid_height = 1 * self.btn_height
        self.current_item_grid_width = self.window_width
        self.current_item_grid_height = 0.07 * self.window_height
        self.top_area_width = self.window_width
        self.top_area_height = self.window_height - self.current_item_grid_height - self.btn_1st_grid_height

    def clicked_exit(self):
        logger.debug('clicked_exit()')
        self.destroy()


def main():
    # CashPointTester().mainloop()
    # CashPointGridTest1(numerator=1, denominator=2, center=False).mainloop()
    CashPointTest(numerator=2, denominator=3, center=True, rows=5, cols=5).mainloop()

if __name__ == '__main__':
    main()
