# coding=utf-8
"""
Basiert auf Python vKbF, Kapitel 6, Seite 196
"""


def säubern(zeit_string):
    """
    Die Funktion säubern() formatiert einen Zeitstring für Minuten und Sekunden so um, dass statt "-" oder ":" nur noch
    "." als Trennzeichen verwendet wird.
    :param zeit_string: string einer Zeitangabe in Minuten und Sekunden als 'm:ss' oder 'm:ss' oder 'm-ss'
    :return: der string im Format 'm.ss'
    """
    if '-' in zeit_string:
        trenner = '-'
    elif ':' in zeit_string:
        trenner = ':'
    else:
        return(zeit_string)
    (mins, seks) = zeit_string.split(trenner)
    return(mins + '.' + seks)


class Sportler:
    """
    Die Klasse Sportler verwaltet alle Methoden zum Sportler, dessen Zeiten zu erfassen sind.
    Methoden: top3, neue_zeit, neue_zeiten
    """
    def __init__(self, ein_name, ein_geb=None, ein_zeiten=[]):
        self.name = ein_name
        self.geb = ein_geb
        self.zeiten = ein_zeiten
        
    def top3(self):
        """
        Gibt die 3 besten Zeiten eines Sportlers als Liste zurück.
        :return: Liste der 3 schnellsten Zeiten
        """
        return(sorted(set([säubern(t) for t in self.zeiten]))[0:3])

    def neue_zeit(self, ein_wert):
        """
        Fügt dem Sportler eine neue Zeit hinzu.
        :param ein_wert: Zeit als string
        :return:
        """
        self.zeiten.append(säubern(ein_wert))

    def neue_zeiten(self, ein_liste):
        """
        Fügt dem Sportler eine Anzahl von Zeiten hinzu
        :param ein_liste: Liste mit Zeiten-strings
        :return:
        """
        for ein_wert in ein_liste:
            self.neue_zeit(ein_wert)


def datei_lesen(dateiname):
    """
    Liest eine Komme-separierte Textdatei und erstellt ein passende Sportler-Objekt daraus
    Erwartetes Format: 1. Wert = Name, 2. Wert = Geburtsdatum, ab dem 3. Wert: Ergebniszeiten
    :param dateiname: Name der einzulesenden Datei
    :return: Objekt Sportler()
    """
    try:
        with open(dateiname) as f:
            daten = f.readline()
        templ = daten.strip().split(',')
        return(Sportler(templ.pop(0), templ.pop(0), templ))
    except IOError as ioerr:
        print('Dateifehler: ' + str(ioerr))
        return(None)
    
ron = datei_lesen('ron2.txt')
sarah = datei_lesen('sarah2.txt')
mark = datei_lesen('mark2.txt')
julie = datei_lesen('julie2.txt')

print(ron.name + "s Bestzeiten sind: " + str(ron.top3()))

ron.neue_zeit('1.58')
print(ron.name + "s Bestzeiten sind: " + str(ron.top3()))

print(sarah.name + "s Bestzeiten sind: " + str(sarah.top3()))

sarah.neue_zeiten(['2.15', '2-19'])
print(sarah.name + "s Bestzeiten sind: " + str(sarah.top3()))

print(mark.name + "s Bestzeiten sind: " + str(mark.top3()))
print(julie.name + "s Bestzeiten sind: " + str(julie.top3()))
