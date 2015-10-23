# -*- coding: utf-8 -*-
__author__ = 'pwust'
# Package 
# Version 

"""Dies ist das Modul "schachtler.py". Es stellt eine Funktion namnes print_lvl()
bereit, die eine Liste mit beliebig vielen eingebetteten Listen ausgibt."""


def print_lvl(liste, einruecken=False, ebene=0):
    """Diese Funktion erwartet ein positionelles Argument namens "liste", das eine
        beliebige Python-Liste (mit eventuell eingebetteten Listen) ist. Jedes Element der
        Liste wird (rekursiv) auf dem Bildschirm jeweils in einer eigenen Zeile ausgegeben.
        Das zweite Argument "einruecken" bestimmt, ob oder ob nicht eingerückt werden soll
        (standard = False = nein).
        Mit dem dritten Argument "ebene" können bei eingebetteten Listen die Anzahl der
        Anfangs-Tabulatoren setzen (standard = 0 = keine Anfangseinrückung)."""
    for element in liste:
        if isinstance(element, list):
            print_lvl(element, einruecken, ebene + 1)
        else:
            if einruecken:
                for tab in range(ebene):
                    print("\t", end='')
            print(element)

