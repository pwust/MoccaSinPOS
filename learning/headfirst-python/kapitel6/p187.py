class Sportler:
    def __init__(self, value=0):
        # Code zur Initialisierung eines "Sportler"-Objekts.
        self.ding = value

    def wie_groß(self):
        return(len(self.ding))


    def säubern(zeit_string):
        if '-' in zeit_string:
            trenner = '-'
        elif ':' in zeit_string:
            trenner = ':'
        else:
            return(zeit_string)
        (mins, seks) = zeit_string.split(trenner)
        return(mins + '.' + seks)

    def datei_lesen(dateiname):
        try:
            with open(dateiname) as f:
                daten = f.readline()
            templ = daten.strip().split(',')
            return({'Name'  : templ.pop(0),
                    'Geb'   : templ.pop(0),
                    'Zeiten': str(sorted(set([säubern(t) for t in templ]))[0:3])})
        except IOError as ioerr:
            print('Dateifehler: ' + str(ioerr))
            return(None)

x = Sportler("Holy Grail")

print(x.wie_groß())

exit()

a = Sportler()
b = Sportler()
c = Sportler()
d = Sportler()


ron = a.datei_lesen('ron2.txt')
sarah = b.datei_lesen('sarah2.txt')
mark = c.datei_lesen('mark2.txt')
julie = d.datei_lesen('julie2.txt')

print(ron['Name'] + "s Bestzeiten sind: " + ron['Zeiten'])
print(sarah['Name'] + "s Bestzeiten sind: " + sarah['Zeiten'])
print(mark['Name'] + "s Bestzeiten sind: " + mark['Zeiten'])
print(julie['Name'] + "s Bestzeiten sind: " + julie['Zeiten'])
