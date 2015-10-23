# -*- coding: utf-8 -*-
__author__ = 'pwust'
# Package 
# Version 

import os


def säubern(zeit_string):
    if '-' in zeit_string:
        trenner = '-'
    elif ':' in zeit_string:
        trenner = ':'
    else:
        return zeit_string
    (mins, seks) = zeit_string.split(trenner)
    return (mins + '.' + seks)


try:
    os.chdir('c:\\src\\pwust\\PycharmProjects\\MoccaSinPOS\\learning\\headfirst-python\\kapitel5\\')

    # for MyName in ('ron', 'julie', 'sarah', 'mark'):
    try:
        with open('ron.txt', 'r') as datei_ron, open('julie.txt', 'r') as datei_julie, \
                open('mark.txt', 'r') as datei_mark, open('sarah.txt', 'r') as datei_sarah:
            daten_ron = datei_ron.readline().strip().split(',')
            daten_julie = datei_julie.readline().strip().split(',')
            daten_mark = datei_mark.readline().strip().split(',')
            daten_sarah = datei_sarah.readline().strip().split(',')

            print('---U-N-S-O-R-T-E-D-----------------------')

            print('Ron:  ', daten_ron)
            print('Julie:', daten_julie)
            print('Mark: ', daten_mark)
            print('Sarah:', daten_sarah)

            print('---N-O-R-M-A-L-I-Z-E-D-------------------')

            ron_sauber = []
            jul_sauber = []
            mar_sauber = []
            sar_sauber = []

            for item in daten_ron:
                ron_sauber.append(säubern(item))
            for item in daten_julie:
                jul_sauber.append(säubern(item))
            for item in daten_mark:
                mar_sauber.append(säubern(item))
            for item in daten_sarah:
                sar_sauber.append(säubern(item))

            print('Ron:  ', ron_sauber)
            print('Julie:', jul_sauber)
            print('Mark: ', mar_sauber)
            print('Sarah:', sar_sauber)

            print('---S-O-R-T-E-D---------------------------')

            print('Ron:  ', sorted(ron_sauber))
            print('Julie:', sorted(jul_sauber))
            print('Mark: ', sorted(mar_sauber))
            print('Sarah:', sorted(sar_sauber))

    except IOError as IOerr:
        print('IOError: ', str(IOerr))

    except:
        print('Anderer Fehler...')

except:
    print('Pfad nicht gefunden!')
