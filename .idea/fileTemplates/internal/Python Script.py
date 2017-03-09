# -*- coding: utf-8 -*-
import logging
import tkinter

__project__ = '${PROJECT_NAME}'
__author__ = '${USER}'
__created__ = '${DATE}-${TIME}'

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)-15s %(name)-5s %(levelname)-8s %(message)s')
#                   levels: CRITICAL 50, ERROR 40, WARNING 30, INFO 20, DEBUG 10, NOTSET 0

logger = logging.getLogger('${NAME}')


def main():
    pass


if __name__ == '__main__':
    main()

