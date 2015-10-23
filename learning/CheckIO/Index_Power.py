# -*- coding: utf-8 -*-
__author__ = 'pwust'
# Package 
# Version 


def index_power(array, n):
    """
        Find Nth power of the element with index N.
    """
    if len(array) <= n:
        return -1
    elif n == 0:
        return 1
    else:
        result = array[n]
        for i in range(n-1):
            result = result * array[n]
        return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
    assert index_power([96, 92, 94], 3) == -1, "IndexError"

