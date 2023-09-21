#!/usr/bin/python3
"""
function determining the fewest number of coins neede to meet a given amount.
"""


def makeChange(coins, total):
    """
    make change.
    Args: coins - kist of values of coins in possession
          total - amount
    Return: fewest number  of coins
    """
    tmp = 0
    coins.sort(reverse=True)

    if total < 0:
        return (0)

    for coin in coins:
        if total % coin <= total:
            tmp += total // coin
            total = total % coin
    return tmp if total == 0 else -1
