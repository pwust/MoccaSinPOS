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
    return mins + '.' + seks


with open('ron.txt') as rod:
    daten = rod.readline()
ron = daten.strip().split(',')
with open('julie.txt') as jud:
    daten = jud.readline()
julie = daten.strip().split(',')
with open('mark.txt') as mad:
    daten = mad.readline()
mark = daten.strip().split(',')
with open('sarah.txt') as sad:
    daten = sad.readline()
sarah = daten.strip().split(',')

ron_sauber = sorted([säubern(zeit) for zeit in ron])
julie_sauber = sorted([säubern(zeit) for zeit in julie])
mark_sauber = sorted([säubern(zeit) for zeit in mark])
sarah_sauber = sorted([säubern(zeit) for zeit in sarah])

print('Ron  :', ron_sauber)
print('Julie:', julie_sauber)
print('Mark :', mark_sauber)
print('Sarah:', sarah_sauber)
print('---TOP3---')
print('Ron  :', ron_sauber[0:3])
print('Julie:', julie_sauber[0:3])
print('Mark :', mark_sauber[0:3])
print('Sarah:', sarah_sauber[0:3])


for i in range(3):
    if ron_sauber[i] == ron_sauber[i+1]:
        ron_sauber.pop(i)
    if julie_sauber[i] == julie_sauber[i+1]:
        julie_sauber.pop(i)
    if mark_sauber[i] == mark_sauber[i+1]:
        mark_sauber.pop(i)
    if sarah_sauber[i] == sarah_sauber[i+1]:
        sarah_sauber.pop(i)

print('---TOP3---')
print('Ron  :', ron_sauber)
print('Ron  :', ron_sauber[0:3])
print('Julie:', julie_sauber)
print('Julie:', julie_sauber[0:3])
print('Mark :', mark_sauber)
print('Mark :', mark_sauber[0:3])
print('Sarah:', sarah_sauber)
print('Sarah:', sarah_sauber[0:3])
