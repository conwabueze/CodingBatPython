"""

Given a string, return a new string where the first and last chars have been exchanged.
"""


def front_back(str):
    if len(str) < 2:
        return str

    str_first = str[0]
    str_middle = str[1:len(str) - 1]
    str_last = str[len(str) - 1]
    return str_last + str_middle + str_first