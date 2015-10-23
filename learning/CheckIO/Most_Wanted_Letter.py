# -*- coding: utf-8 -*-
__author__ = 'pwust'
# Package 
# Version 

def checkio(text):
    """
    If you have two or more letters with the same frequency, then return the letter which comes first in
    the latin alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".
    :param text:  A text for analysis as a string
    :return: The most frequent letter in lower case as a string.
     Example:
        checkio("Hello World!") == "l"
        checkio("How do you do?") == "o"
        checkio("One") == "e"
        checkio("Oops!") == "o"
        checkio("AAaooo!!!!") == "a"
        checkio("abe") == "a"
    """
    text = text.lower()
    counter = {}
    alfabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in (alfabet):
        counter[i] = 0
    for character in text:
        if character in alfabet:
            counter[character] = counter[character] + 1
            #print(character + "\t" + str(counter[character]))
    maxnum = 0
    maxwl = 0

    for letter in alfabet:
        if counter[letter] > maxnum:
            maxnum = counter[letter]
            maxwl = letter
    return (maxwl)



test = "Aa Bb xsaDFI123hwfu!,:;ä aa"

print(test)
print(checkio(test))
