__author__ = 'pwust'

import time


def ganz_viele_Zahlen(max):
    t1 = time.time()
    for x in range(0, max):
        print(x, end='' )
        if (x % 50 == 0):
            print()
        else:
            print(end=' ')
    print()
    t2 = time.time()
    print ('Es hat %s Sekunden gebraucht' % (t2-t1))

ziel = 1

while (ziel != 0):
    ziel = int(input('Wie viele Zahlen (0=Ende)?'))
    ganz_viele_Zahlen(ziel)



