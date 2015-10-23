#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'pwust'
# Package 
# Version 

import sportlermodell
import yate
import cgi
# import cgitb

# cgitb.enable()

alle_sportler = sportlermodell.konserve_lesen()

form_daten = cgi.FieldStorage()
sportler_name = form_daten['sportlerwahl'].value

print(yate.antwort_anfang())
print(yate.seitenanfang('Trainer Tims Laufzeiten'))
print(yate.heading('Das sind die Bestzeiten von ' + sportler_name + ':'))
print(yate.u_liste(alle_sportler[sportler_name].top3))
# print(yate.u_liste(alle_sportler[sportler_name].top3()))
print(yate.seitenende({'Home': '/index.html',
                       'anderen Sportler wählen': 'liste_generieren.py'}))


