__author__ = 'pwust'
# -*- coding: utf-8 -*-


def printall(liste):
    if isinstance(liste, list):
        for myitem in liste:
            if isinstance(myitem, list):
                printall(myitem)
            else:
                print(myitem)
    else:
        print(liste)


filme = ['Die Ritter der Kokosnuss', 1975, "Terry Jones & Terry Gilliam", 91,
         ["Graham Chapman", ["Michael Palin", "John Cleese",
                             "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

print(">>>> Schnöde Ausgabe:")
print(filme)
print(">>>> Aufgedröselte Ausgabe:")
printall(filme)

nichtarray = "Ich bin nur ein Text."
print(">>>> Jetzt ein simpler String:")
printall(nichtarray)

buchstabe = "X"
print(">>>> Nur ein Buchstabe:")
printall(buchstabe)

zahl=10
print(">>>> Nur eine Zahl:")
printall(zahl)
