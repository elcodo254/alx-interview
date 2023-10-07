#!/usr/bin/python3
"""
Given a number n, write a method that calcuates the fewest number of
/operations needed to result in exactly n H(single character in text file)
/characters in the file.
"""


def countProcess(num):
    """ Return list of process until n H """
    count = 1
    p_list = []
    val = num
    while val != 1:
        count += 1
        if val % count == 0:
            while (val % count == 0 and val != 1):
                val /= count
                p_list.append(count)

    return p_list

def minOperations(n):
    """
    method that returns minimum operation to get n Hs
    """
    if n < 2 or type(n) is not int:
        return 0
    values = countProcess(n)
    return sum(values)
