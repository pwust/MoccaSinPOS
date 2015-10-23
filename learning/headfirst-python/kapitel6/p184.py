# -*- coding: utf-8 -*-
__author__ = 'pwust'
# Package 
# Version 


def säubern(zeit_string):
    """
    Die Funktion säubern() nimmt eine Zeitangabe mit Minuten und Sekunden als Text an,
    und wandelt die Zeit vom Format 1:23 oder 1-23 in das Format 1.23 um.

    :param zeit_string: Eine Zeichenkette in einem der oben genannten Formate.
    :return: Eine Zeciehnkette im Format 1.23 (für 1 Minute 23 Sekunden)
    """
    if '-' in zeit_string:
        trenner = '-'
    elif ':' in zeit_string:
        trenner = ':'
    else:
        return(zeit_string)
    (mins, seks) = zeit_string.split(trenner)
    return (mins + '.' + seks)


def datei_lesen(dateiname):
    """
    datei_lesen liest eine Textdatei ein, deren Inhalt in einer Zeile verschiedene durch Komma getrennt Were enthält.

    :param dateiname: Die einzulesende Datei mit Komma-separierten Daten
    :return: eine Liste mit allen Werten
    """
    try:
        with open(dateiname) as f:
            daten = f.readline()
        templ = daten.strip().split(',')
        return ({'Name' : templ.pop(0),
                 'Geb' : templ.pop(0),
                 'Zeiten' : str(sorted(set([säubern(t) for t in templ]))[0:3])
                 })
    except IOError as ioerr:
        print('Dateifehler: ' + str(ioerr))
        return(None)

def auswerten(dateiname):
    """
    die Funktion auswerten() fasst die Sportler-Auswertung zusammen: Einlesen der rohdaten aus einer Datei,
    Zusammenfassen, sortieren und Ausgabe der Top 3 Zeiten mit dem Namen des Sportlers.

    :param dateiname:
    :return:
    """
    try:
        sportler = datei_lesen(dateiname)
        #(sportler_name, sportler_geb) = sportler.pop(0), sportler.pop(0)
        print(sportler['Name'] + 's Bestzeiten sind: ' + sportler['Zeiten'])
    except AttributeError as attrerr:
        pass
        #print('Attributfehler: ' + str(attrerr))

for datei in ('sarah2.txt', 'ron2.txt', 'mark2.txt', 'julie2.txt'):
    auswerten(datei)
