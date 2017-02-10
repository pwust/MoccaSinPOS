# -*- coding: utf-8 -*-
__author__ = 'Patric Wust'
# Package 
# Version
"""
Module: readprices
Load price data from MoccaSin's old price
and verify its correctness, respectively
show parts that need reworking.
"""

import os
import re


class Prices():
    """
        Aufbau product.ini und ausnahme.ini
        Comme seprated values
        Kommentarzeilen:
            Line comment startet mit @
        Aufbau Produkte "DEF":
        z.B. "DEF,136,Eiskaffee"
            "DEF,201,klein"
            "DEF,318,Chai Chocolate"
            "DEF,401,to go"
        -> 3 Felder:
        1: "DEF"
        2: Nummer dreistellig 1##, 2##, 3## oder 4##
            2a: 1## = Warengruppe
            2b: 2## = Größe
            2c: 3## = Produkt/Variante
            2d: 4## = Darreichungsform
        3: Bezeichnung
        --
        Aufbau Tastenfeld "LABEL":
        z.B. "LABEL,101,BLACK,Espresso+101		,groß+203 klein+201		,Originale+301 Barista+302 Cuba+303 Lungo+304 Unplugged+305 Macchiato+306 Orange+310,"
        -> 6 Felder:
        1: "LABEL"
        2: xy-pos der Taste:
            101 = 1. Reihe ganz links, 102 = 2. Reihe ganz links, .. 108 = 8. Reihe ganz links
            109 = 1. Reihe 2. Knopf, 110 = 2. Reihe 2. Knopf, ...
            117 = 1. Reihe 3. Knopf, ...
            125 = 1. Reihe 4. Knopf, ...
            133 = 1. Reihe 5. Knopf, ...
            141 = 1. Reihe 6. Knopf, ...
        3: Farbe der Taste (BLACK, BLUE, BROWN, DMAG, KACK, LGREEN)
        4: Beschriftung Haupttaste, "+", Warengruppennummer
        5: Beschriftung Größentaste, "+", Größennummer
        6: Beschriftung Variantentaste, "+", Prokukt/Variantennummer
        --
        Aufbau Preisangabe "PREIS":
        z.B. "PREIS,100200300402,1.00"
        -> 3 Felder
        1. "PREIS"
        2. Artikelnummer 1##2##3##4##
        3. Preis angabe (Dezimaltrenner = Punkt)
        """
    ConfigPath = os.path.join('.', 'old-moc-data', 'umsatz')

    products_filename=os.path.join(ConfigPath, 'product.ini')
    ausnahme_filename=os.path.join(ConfigPath, 'ausnahme.ini')

    # product_prices = {}
    # product_names = {}
    # product_labels = {}
    # product_raw = []
    # exception_raw = []

    def __init__(self):
        self.product_prices = {}
        self.product_names = {}
        self.product_labels = {}
        self.product_raw = []
        self.exception_raw = []
        self.exception_prices = {}


    def ReadProductsFromFile(self, productsfilename='product.ini', exceptionsfilename='ausnahme.ini'):
        """
        Liest die Liste aller Produkte aus den beiden Produkt-Dateien (normalerweise "product.ini" und "ausnahme.ini"
        :param productsfilename: default = 'product.ini'
        :param exceptionsfilename: default = 'ausnahme.ini'
        :return:
        """
        all_lines_count = 0
        good_lines_count = 0
        price_lines_count = 0
        name_lines_count = 0
        label_lines_count = 0
        double_lines_count = 0

        # global product_prices
        # global product_names
        # global product_labels

        print(productsfilename + ':')
        with open(productsfilename, 'r') as file:
            for line in file:
                line = line.rstrip("\r\n\t ")
                all_lines_count += 1
                if not (re.match('^(\s*|\s*@+.*)$',line)):
                    # ignoring empty lines and commented lines
                    good_lines_count += 1
                    self.product_raw.append(line)
                    if line.split(',')[0] == 'PREIS':
                        if line.split(',')[1] in self.product_prices:
                            print()
                            print('Key %s already stored! (existing: %s, not-stored: %s)' %
                                  (line.split(',')[1],self.product_prices[line.split(',')[1]],line.split(',')[2]))
                            double_lines_count += 1
                        else:
                            self.product_prices[line.split(',')[1]] = line.split(',')[2]
                            if __name__ == '__main__':
                                print('p', end='')
                            price_lines_count += 1
                    elif line.split(',')[0] == 'DEF':
                        self.product_names[line.split(',')[1]] = line.split(',')[2]
                        if __name__ == '__main__':
                            print('d', end='')
                        name_lines_count += 1
                    elif line.split(',')[0] == 'LABEL':
                        self.product_labels[line.split(',')[1]] = line.split(',',2)[2]
                        if __name__ == '__main__':
                            print('l', end='')
                        label_lines_count += 1
                pass
            if __name__ == '__main__':
                print()
                print()
                print('Number of lines: %s (%s good ones, %s prices, %s groups, %s labels, %s double).' %
                      (all_lines_count, good_lines_count, price_lines_count, name_lines_count, label_lines_count, double_lines_count))
                #print('Object lengths: %s prices, %s groups, %s labels.' % (len(product_prices), len(product_names), len(product_labels)))

        all_lines_count = 0
        good_lines_count = 0
        price_lines_count = 0
        double_lines_count = 0

        print(exceptionsfilename + ':')
        with open(exceptionsfilename, 'r') as file:
            for line in file:
                line = line.rstrip("\r\n\t ")
                all_lines_count += 1
                if not (re.match('^(\s*|\s*@+.*)$',line)):
                    # ignoring empty lines and commented lines
                    good_lines_count += 1
                    self.exception_raw.append(line)
                    if line.split(',')[0] == 'PREIS':
                        if line.split(',')[1] in self.exception_prices:
                            print()
                            print('Key %s already stored! (existing: %s, not-stored: %s)' %
                                  (line.split(',')[1],self.exception_prices[line.split(',')[1]],line.split(',')[2]))
                            double_lines_count += 1
                        else:
                            self.exception_prices[line.split(',')[1]] = line.split(',')[2]
                            if __name__ == '__main__':
                                print('p', end='')
                            price_lines_count += 1
                pass
            if __name__ == '__main__':
                print()
                print()
                print('Number of lines: %s (%s good ones, %s prices, %s double).' %
                      (all_lines_count, good_lines_count, price_lines_count, double_lines_count))
                #print('Object lengths: %s prices, %s groups, %s labels.' % (len(product_prices), len(product_names), len(product_labels)))

def main():
    alles = Prices()
    # alles.ReadProductsFromFile(os.path.abspath(os.path.join('..', 'old-moc-data', 'umsatz', 'product.ini')),
    #                             os.path.abspath(os.path.join('..', 'old-moc-data', 'umsatz', 'ausnahme.ini')))
    alles.ReadProductsFromFile(os.path.abspath(os.path.join('c:\\', 'private', 'moc', 'dur', 'umsatz', 'product.ini')),
                                os.path.abspath(os.path.join('c:\\', 'private', 'moc', 'dur', 'umsatz', 'ausnahme.ini')))
    #print(Prices.product_prices)


if __name__ == '__main__':
    main()
