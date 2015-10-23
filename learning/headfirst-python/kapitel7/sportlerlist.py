# -*- coding: utf-8 -*-
__author__ = 'pwust'
# Package 
# Version 


def säubern(zeit_string):
    if '-' in zeit_string:
        trenner = '-'
    elif ':' in zeit_string:
        trenner = ':'
    else:
        return(zeit_string)
    (mins, seks) = zeit_string.split(trenner)
    return(mins + '.' + seks)


class SportlerList(list):
    """
    Diese Klasse erweitert ein Standard-Listenobjekt um die Attribute "name" und "geb"

    Attribute:
    self.name = Name des Sportlers.
    self.geb = Geburtsdatum des Sportlers.
    self = Liste mit den eizelnen Laufzeiten des Sportlers.

    Methoden:
    self.top3 gibt die drei schnellsten Zeiten als String-Liste zurück.

    """
    def __init__(self, ein_name, ein_geb=None, ein_zeiten=[]):
        list.__init__([])
        self.name = ein_name
        self.geb = ein_geb
        self.extend(ein_zeiten)

    def top3(self):
        """
        Gibt die drei schnellsten Zeiten des Sportlers zurück, sofern drei verschiedene
        Zeiten vorhanden sind (sonst ist die Rückgabe-Liste entsprechend kürzer).
        :return: string liste mit drei Zeiten im Format ['m.ss', 'm.ss', 'm.ss']
        """
        return(sorted(set([säubern(t) for t in self]))[0:3])


def datei_lesen(dateiname):
    """
    Liest eine Textdatei ein und gibt ein den Inhalt als Objekt SportlerList zurück.
    :param dateiname:
    :return:
    """
    try:
        with open(dateiname) as f:
            daten = f.readline()
        templ = daten.strip().split(',')
        return(SportlerList(templ.pop(0), templ.pop(0), templ))
    except IOError as ioerr:
        print('Dateifehler: ' + str(ioerr))
        return(None)
