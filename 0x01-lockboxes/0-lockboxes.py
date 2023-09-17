#!/usr/bin/python3
"""
lockboxes problem: You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 /
and may contain keys to the other boxes.
Write a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.
    args: boxes - list of lists
    Description:
                assume all keys will be positive and some don't have boxes.
                first box is unlocked
    Return: True if all can be opened otherwise False
    """
    keys = [0]
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    if len(keys) == len(boxes):
        return True
    return False
