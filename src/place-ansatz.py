# coding=utf-8
import tkinter as tk
from tkinter import ttk
import logging
from tkinter import font as tkfont

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

    def __init__(self, parent=None, numerator=3, denominator=4, center=True):
        tk.Tk.__init__(self, parent)
        self.numerator = numerator
        self.denominator = denominator
        self.center = center
        # fonts
        logger.debug('tkfont.families = {}'.format(tkfont.families()))
        self.fnt_arial_r_24_bi = tkfont.Font(family='Arial Rounded MT Bold', size=24, weight='bold', slant='italic')
        self.fnt_courier_24_bi = tkfont.Font(family='Courier New', size=24, weight='bold', slant='italic')
        self.fnt_ocr_a_24_b = tkfont.Font(family='OCR A Extended', size=24, weight='bold')
        self.fnt_ocr_a_12_b = tkfont.Font(family='OCR A Extended', size=12, weight='bold')
        self.fnt_lucida_c_20_b = tkfont.Font(family='Lucida Console', size=20, weight='bold')
        self.fnt_lucida_c_12_b = tkfont.Font(family='Lucida Console', size=12, weight='bold')
        self.fnt_lucida_c_def = tkfont.Font(family='Lucida Console')
        # class internal variables:
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
        self.top_area_grid_width = 0
        self.screen_width = 0
        self.screen_height = 0
        self.offset_x = 0
        self.offset_y = 0
        self.col_width = 0
        self.row_height = 0
        self.my_current_item = {}
        self.init_app()

    def init_app(self):
        # determine screen size
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        logger.debug('screen size = %sx%s' % (self.screen_width, self.screen_height))

        logger.debug('factor for window size used: {}/{}, centering = {}'
                     .format(self.numerator, self.denominator, self.center))

        self.window_width = self.numerator * self.screen_width // self.denominator  # 3/4 of the screen size used
        self.window_height = self.numerator * self.screen_height // self.denominator  # 3/4 of the screen size used
        logger.debug('window size = %sx%s' % (self.window_width, self.window_height))

        if self.center:
            self.offset_x = (self.screen_width - self.window_width) // 2  # centered
            self.offset_y = (self.screen_height - self.window_height) // 2  # centered
        else:
            self.offset_x = 0
            self.offset_y = 0
        logger.debug('offset      = %sx%s' % (self.offset_x, self.offset_y))

        self.geometry(newGeometry='{}x{}+{}+{}'
                      .format(self.window_width, self.window_height, self.offset_x, self.offset_y))

        self.recalc_sizes()

        # move window to center of available screen
        #        self.geometry(newGeometry='{}x{}+{}+{}'.format(window_width, window_height, offset_x, offset_y))

        # self.minsize(width=self.window_width // 2, height=self.window_height // 2)
        # self.maxsize(width=self.screen_width, height=self.screen_height)

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
        frm_app.rowconfigure(0, weight=1)
        frm_app.columnconfigure(0, weight=1)
        # frm_app.grid_propagate(0)
        # logger.debug('frm_app: {}'.format(frm_app.grid_info()))

        # todo sizes in frm_app

        # putting in percentages for the GUI sizes of the subframes
        frm_app.rowconfigure(0, weight=19)  # top area
        frm_app.rowconfigure(1, weight=7)   # current item area
        frm_app.rowconfigure(2, weight=63)  # button area, upper part
        frm_app.rowconfigure(3, weight=9)   # button area, lower part (user info in column 1)

        frm_app.columnconfigure(0, weight=54)  # 6 * 9
        frm_app.columnconfigure(1, weight=27)  # 3 * 9
        frm_app.columnconfigure(1, weight=19)  # 100 - (6*9 + 3*9))




        # TOP AREA: Logo, Menu Button, Receipt Display,
        # todo TOP AREA

        frm_display = ttk.LabelFrame(frm_app, text=' Top Area ')
        frm_display.grid(column=0, row=0, columnspan=3, rowspan=1, sticky='ew')
        frm_display.rowconfigure(0, weight=100)

        # todo sizes within top area:
        # Logo = 1/8, Menu = 1/8, Bill = 5/8, buttons = 1/8
        frm_display.columnconfigure(0, weight=125)  # Logo
        frm_display.columnconfigure(1, weight=125)  # Menu
        frm_display.columnconfigure(2, weight=625)  # Receipt
        frm_display.columnconfigure(3, weight=125)  # Buttons

        logger.debug('frm_display is of class {}'.format(frm_display.winfo_class()))
        btn_menu = ttk.Button(frm_display, text='EXIT', command=self.clicked_exit)
        btn_menu.grid(column=1, row=0, sticky='nsew')

        # todo CURRENT ITEM AREA
        # todo make this one a text widget (distinct formatting, etc.)

        self.my_current_item['text'] = tk.StringVar()
        self.my_current_item['text'].set('Hallo, Test...')
        frm_current_item = ttk.Frame(frm_app)  # , text=' Current Item ')
        frm_current_item.grid(column=0, row=1, columnspan=3, sticky='nsew')
        frm_current_item.rowconfigure(0, weight=100)
        frm_current_item.columnconfigure(0, weight=100)
        lbl_current_item = ttk.Label(frm_current_item, textvariable=self.my_current_item['text'])
        lbl_current_item.grid(row=0, column=0, sticky='nsew')
        logger.debug('width of label = {}'.format(lbl_current_item.winfo_width()))
        # lbl_current_item.configure(font=self.fnt_arial_r_24_b)
        # lbl_current_item.configure(font=self.fnt_courier_24_b)
        # lbl_current_item.configure(font=self.fnt_lucida_c_20_b)
        lbl_current_item.configure(font=self.fnt_lucida_c_def)

        # todo 1ST BUTTON AREA
        frm_1st_buttons = ttk.Frame(frm_app)  # , text=' Level 1 ')
        frm_1st_buttons.grid(column=0, row=2, rowspan=2, sticky='nsew')
        # frm_1st_buttons.rowconfigure(0, weight=1)
        # frm_1st_buttons.columnconfigure(0, weight=1)
        # logger.debug('frm_1st_buttons: {}'.format(frm_1st_buttons.grid_info()))
        for col_index in range(6):  # 6
            frm_1st_buttons.columnconfigure(col_index, weight=1)
            for row_index in range(8):  # 8
                frm_1st_buttons.rowconfigure(row_index, weight=1)
                logger.debug('creating button 1: {}/{}'.format(col_index, row_index))
                cmd = lambda x=col_index, y=row_index: self.button1_callback(x, y)
                btn = ttk.Button(frm_1st_buttons, )
                btn.configure(text="1: {}/{}".format(col_index, row_index))
                btn.configure(command=cmd)
                # btn.configure(width=self.btn_width // 10, height=self.btn_height // 20)
                btn.grid(row=row_index, column=col_index, sticky='nsew')

        # todo 2ND BUTTON AREA

        frm_2nd_buttons = ttk.Frame(frm_app)  # , text=' Level 2 ')
        frm_2nd_buttons.grid(column=1, row=2, sticky='nsew')
        # frm_2nd_buttons.rowconfigure(0, weight=1)
        # frm_2nd_buttons.columnconfigure(0, weight=1)
        # logger.debug('frm_2nd_buttons: {}'.format(frm_2nd_buttons.grid_info()))
        for col_index in range(3):
            frm_2nd_buttons.columnconfigure(col_index, weight=1)
            for row_index in range(7):
                frm_2nd_buttons.rowconfigure(row_index, weight=1)
                logger.debug('creating button 2: {}/{}'.format(col_index, row_index))
                # tk.Button(frm_2nd_buttons, text='---')
                cmd = lambda x=col_index, y=row_index: self.button2_callback(x, y)
                btn = ttk.Button(frm_2nd_buttons, )
                btn.configure(text='2: {}/{}'.format(col_index, row_index))
                btn.configure(command=cmd)
                # btn.configure(width=self.btn_width // 10, height=self.btn_height // 20)
                btn.grid(row=row_index, column=col_index, sticky='nsew')

        # todo CURRENT USER AREA

        frm_user_display = ttk.LabelFrame(frm_app, text=' User Info ')
        frm_user_display.grid(column=1, row=3, sticky='ew')
        # frm_user_display.grid_propagate(0)
        # logger.debug('frm_user_display: {}'.format(frm_user_display.grid_info()))
        # ttk.Button(frm_user_display, text='tmpBtn').grid(column=0, row=0)
        tk.Label(frm_user_display, text='Angemeldeter Bediener:').grid(column=0, row=0, sticky='ew')
        lbl_active_user = tk.Label(frm_user_display, text='BEDIENER - ??')
        lbl_active_user.grid(column=0, row=1, sticky='ew')
        # lbl_active_user.configure(style='Userinfo.TLabel')

        # todo 3RD BUTTON AREA

        frm_3rd_buttons = ttk.LabelFrame(frm_app, text=' Level 3 ')
        frm_3rd_buttons.grid(column=2, row=2, rowspan=2, sticky='ns')
        # logger.debug('frm_3rd_buttons: {}'.format(frm_3rd_buttons.grid_info()))
        ttk.Button(frm_3rd_buttons, text='tmpBtn').grid(column=0, row=0, columnspan=2)

    def button1_callback(self, x, y):
        logger.debug('button L1/{:2}/{:2} pressed.'.format(x, y))
        self.my_current_item['text'].set('{} L{}:{}/{}'.format(self.my_current_item['text'].get(), 1, x, y ))

    def button2_callback(self, x, y):
        logger.debug('button L2/{:2}/{:2} pressed.'.format(x, y))

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
        - top area with receipt, logo, etc = 19% (113px)
        - top area has 1/8 grid: 1 logo, 1 menu button, 5 receipt, 1 buttons
        :return:
        """
        # self.window_width = int(self.winfo_screenwidth())
        # self.window_height = int(self.winfo_screenheight())
        self.btn_width = int(.09 * self.window_width)
        self.btn_height = int(.09 * self.window_height)
        self.btn_1st_grid_width = int(6 * self.btn_width)
        self.btn_1st_grid_height = int(8 * self.btn_height)
        self.btn_2nd_grid_width = int(3 * self.btn_width)
        self.btn_2nd_grid_height = int(7 * self.btn_height)
        self.btn_3rd_grid_width = int(self.window_width - self.btn_1st_grid_width - self.btn_2nd_grid_width)
        self.btn_3rd_grid_height = int(self.btn_1st_grid_height)
        self.userinfo_grid_width = int(self.btn_2nd_grid_width)
        self.userinfo_grid_height = int(1 * self.btn_height)
        self.current_item_grid_width = int(self.window_width)
        self.current_item_grid_height = int(0.07 * self.window_height)
        self.top_area_width = int(self.window_width)
        self.top_area_height = int(self.window_height - self.current_item_grid_height - self.btn_1st_grid_height)
        self.top_area_grid_width = int(self.top_area_width / 8)

    def clicked_exit(self):
        logger.debug('clicked_exit()')
        self.destroy()


def main():
    # CashPointTester().mainloop()
    # CashPointGridTest1(numerator=1, denominator=2, center=False).mainloop()
    CashPointTest(numerator=2, denominator=3, center=True).mainloop()

if __name__ == '__main__':
    logger.info('Script started.')
    main()
    logger.info('Script exited.')
