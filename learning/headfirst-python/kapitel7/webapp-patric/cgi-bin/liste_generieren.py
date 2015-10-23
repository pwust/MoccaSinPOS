#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'pwust'
# Package 
# Version 

import sportlermodell
import yate
import glob

datendateien = glob.glob('daten/*.txt')

alle_sportler = sportlermodell.konserve_machen(datendateien)

print(yate.antwort_anfang())
print(yate.seitenanfang('Die Sportler von Trainer Tim'))
print(yate.form_anfang('zeitdaten_generieren.py'))
print(yate.para('Wählen Sie einen Sportler aus der Liste aus:'))
for sportler in alle_sportler:
    print(yate.radio_button('sportlerwahl', alle_sportler[sportler].name))
print(yate.form_ende('Auswählen'))
print(yate.seitenende({'Home': '/index.html'}))
