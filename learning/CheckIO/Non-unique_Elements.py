# -*- coding: utf-8 -*-
__author__ = 'pwust'
# Package 
# Version 


def checkio(data):
    """
    Trim an array down to its non-unique elements
    :param data: a list of items
    :return: the list where all unique items have been removed
    """
    output=[]
    for item in data:
        if data.count(item) > 1:
            output.append(item)

    return(output)

