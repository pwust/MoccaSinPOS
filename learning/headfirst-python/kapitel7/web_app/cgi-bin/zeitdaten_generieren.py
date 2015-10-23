#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

import cgi

import cgitb
cgitb.enable()

import sportlermodell
import yate

alle_sportler = sportlermodell.konserve_lesen()

form_daten = cgi.FieldStorage()
sportler_name = form_daten['sportlerwahl'].value

print(yate.antwort_anfang())
print(yate.seitenanfang("Trainer Tims Laufzeiten"))    
print(yate.heading("Sportler: " + sportler_name + ", Geb.: " +
                      	alle_sportler[sportler_name].geb + "."))
print(yate.para("Die Bestzeiten für diesen Sportler sind:"))
print(yate.u_liste(alle_sportler[sportler_name].top3))
print(yate.seitenende({"Home": "/index.html",
                        "Anderen Sportler auswählen": "liste_generieren.py"}))
