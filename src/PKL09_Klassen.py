# coding=utf-8
__author__ = 'pwust'


# Python kinderleicht, Chapter 9

class Dinge:
    pass


class Unbelebt(Dinge):
    pass


class Bürgersteig(Unbelebt):
    pass


class Belebt(Dinge):
    pass


class Tiere(Belebt):
    def atmen(self):
        print('Einatmen, dann ausatmen.')

    def bewegen(self):
        print('Und jetzt einen Schritt...')

    def fressen(self):
        print('Mampf!')


class Säugetiere(Tiere):
    def ernähren_nachkommen_mit_milch(self):
        print('Milch ist das einzig Wahre für Säuglinge!')


class Giraffen(Säugetiere):
    def fressen_blätter_von_bäumen(self):
        print('Langer Hals -> hohe Blätter.')


wiegand = Giraffen()
wiegand.bewegen()
wiegand.fressen_blätter_von_bäumen()
