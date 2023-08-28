#!/usr/bin/python3
"""
method that determines if a given data set represents a valid UTF-8 encoding.
Description:
    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer.
"""


def validUTF8(data):
    """
    Determines valididty of utf-8 encoding
    Args:
        data - list of integers
    Returns:
        True if valid utf-8 encoding, false otherwise.
    """

    bit1 = 1 << 7 #checks if significant byte is 1
    bit2 = 1 << 6 #checks id 2nd significant byte is 0
    nbytes = 0    #keeps track of how many 1s before 0 occurs

    if not data or len(data) == 0:
        return True

    for num in data:
        bit = 1 << 7
        if nbytes == 0:
            while (bit & num):
                nbytes += 1
                bit = bit >> 1

            if nbytes == 0:
                continue
            if nbytes == 1 or nbytes > 4:
                return False
        else:

            if not (num & bit1 and not (num & bit2)):
                return False
        nbytes -= 1

    if nbytes:
        return False
    else:
        return True
