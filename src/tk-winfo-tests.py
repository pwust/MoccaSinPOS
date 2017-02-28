# coding=utf-8
import tkinter as tk
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)-15s %(name)-5s %(levelname)-8s %(message)s')
#                   levels: CRITICAL 50, ERROR 40, WARNING 30, INFO 20, DEBUG 10, NOTSET 0

logger = logging.getLogger('test')


class MainApp(tk.Tk):
    def __init__(self, parent=None):
        tk.Tk.__init__(self, parent)
        self.show_me()
        pass

    def show_me(self):
        logger.debug('self.winfo_cells() = {}'.format(self.winfo_cells()))
        logger.debug('self.winfo_children() = {}'.format(self.winfo_children()))
        logger.debug('self.winfo_class() = {}'.format(self.winfo_class()))
        logger.debug('self.winfo_colormapfull() = {}'.format(self.winfo_colormapfull()))
        logger.debug('self.winfo_depth() = {}'.format(self.winfo_depth()))
        logger.debug('self.winfo_exists() = {}'.format(self.winfo_exists()))
        # logger.debug('self.winfo_fpixels() = {}'.format(self.winfo_fpixels()))
        logger.debug('self.winfo_geometry() = {}'.format(self.winfo_geometry()))
        logger.debug('self.winfo_height() = {}'.format(self.winfo_height()))
        logger.debug('self.winfo_id() = {}'.format(self.winfo_id()))
        logger.debug('self.winfo_ismapped() = {}'.format(self.winfo_ismapped()))
        logger.debug('self.winfo_manager() = {}'.format(self.winfo_manager()))
        logger.debug('self.winfo_name() = {}'.format(self.winfo_name()))
        logger.debug('self.winfo_parent() = {}'.format(self.winfo_parent()))
        # logger.debug('self.winfo_pixels() = {}'.format(self.winfo_pixels()))
        logger.debug('self.winfo_pointerx() = {}'.format(self.winfo_pointerx()))
        logger.debug('self.winfo_pointerxy() = {}'.format(self.winfo_pointerxy()))
        logger.debug('self.winfo_pointery() = {}'.format(self.winfo_pointery()))
        logger.debug('self.winfo_reqheight() = {}'.format(self.winfo_reqheight()))
        logger.debug('self.winfo_reqwidth() = {}'.format(self.winfo_reqwidth()))
        # logger.debug('self.winfo_rgb() = {}'.format(self.winfo_rgb()))
        logger.debug('self.winfo_rootx() = {}'.format(self.winfo_rootx()))
        logger.debug('self.winfo_rooty() = {}'.format(self.winfo_rooty()))
        logger.debug('self.winfo_screen() = {}'.format(self.winfo_screen()))
        logger.debug('self.winfo_screencells() = {}'.format(self.winfo_screencells()))
        logger.debug('self.winfo_screendepth() = {}'.format(self.winfo_screendepth()))
        logger.debug('self.winfo_screenheight() = {}'.format(self.winfo_screenheight()))
        logger.debug('self.winfo_screenmmheight() = {}'.format(self.winfo_screenmmheight()))
        logger.debug('self.winfo_screenmmwidth() = {}'.format(self.winfo_screenmmwidth()))
        logger.debug('self.winfo_screenvisual() = {}'.format(self.winfo_screenvisual()))
        logger.debug('self.winfo_screenwidth() = {}'.format(self.winfo_screenwidth()))
        logger.debug('self.winfo_server() = {}'.format(self.winfo_server()))
        logger.debug('self.winfo_toplevel() = {}'.format(self.winfo_toplevel()))
        logger.debug('self.winfo_viewable() = {}'.format(self.winfo_viewable()))
        logger.debug('self.winfo_visual() = {}'.format(self.winfo_visual()))
        logger.debug('self.winfo_visualid() = {}'.format(self.winfo_visualid()))
        logger.debug('self.winfo_vrootheight() = {}'.format(self.winfo_vrootheight()))
        logger.debug('self.winfo_vrootwidth() = {}'.format(self.winfo_vrootwidth()))
        logger.debug('self.winfo_vrootx() = {}'.format(self.winfo_vrootx()))
        logger.debug('self.winfo_vrooty() = {}'.format(self.winfo_vrooty()))
        logger.debug('self.winfo_width() = {}'.format(self.winfo_width()))
        logger.debug('self.winfo_x() = {}'.format(self.winfo_x()))
        logger.debug('self.winfo_y() = {}'.format(self.winfo_y()))
        pass


def main():
    MainApp()
    pass


if __name__ == '__main__':
    main()
