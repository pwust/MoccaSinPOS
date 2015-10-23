# -*- coding: utf-8 -*-

import pickle
from sportlerlist import SportlerList

def datei_lesen(dateiname):
    try:
        with open(dateiname) as f:
            daten = f.readline()
        templ = daten.strip().split(',')
        return(SportlerList(templ.pop(0), templ.pop(0), templ))
    except IOError as ioerr:
        print('Dateifehler: ' + str(ioerr))
        return(None)
    
def konserve_machen(dateiliste):
    alle_sportler = {}
    for datei in dateiliste:
        sp = datei_lesen(datei)
        alle_sportler[sp.name] = sp
    try:
        with open('sportler.pickle', 'wb') as spd:
            pickle.dump(alle_sportler, spd)
    except IOError as ioerr:
        print('Dateifehler (konserve_machen): ' + str(ioerr))
    return(alle_sportler)

def konserve_lesen():
    alle_sportler = {}
    try:
        with open('sportler.pickle', 'rb') as spd:
            alle_sportler = pickle.load(spd)
    except IOError as ioerr:
        print('Dateifehler (konserve_lesen): ' + str(ioerr))
    return(alle_sportler)
