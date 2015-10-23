# -*- coding: utf-8 -*-

class SportlerList(list):
    def __init__(self, ein_name, ein_geb=None, ein_zeiten=[]):
        self.name = ein_name
        self.geb = ein_geb
        self.extend(ein_zeiten)
    @property  
    def top3(self):
        return(sorted(set([säubern(t) for t in self]))[0:3])

def säubern(zeit_string):
    if '-' in zeit_string:
        trenner = '-'
    elif ':' in zeit_string:
        trenner = ':'
    else:
        return(zeit_string)
    (mins, seks) = zeit_string.split(trenner)
    return(mins + '.' + seks)
