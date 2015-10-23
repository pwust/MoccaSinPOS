# -*- coding: utf-8 -*-
__author__ = 'pwust'
# Package 
# Version 

def checkio(list):
    """
    You are given an array of integers. You should find the sum of the elements with even indexes
    (0th, 2nd, 4th...) then multiply this summed number and the final element of the array together.
    Don't forget that the first element has an index of 0.

    For an empty array, the result will always be 0 (zero).

    :param list: A list of integers.
    :return: The number as an integer.
    """
    if len(list) == 0:
        return 0
    else:
        summe = 0
        for index in range(0, len(list), 2):
            summe = summe + list[index]
        return summe * list[-1]


if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30
    assert checkio([1, 3, 5]) == 30
    assert checkio([6]) == 36
    assert checkio([]) == 0
