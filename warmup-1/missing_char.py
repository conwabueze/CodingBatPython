"""

Given a non-empty string and an int n,
 return a new string where the char at index n has been removed.
 The value of n will be a valid index of a char in the original
 string (i.e. n will be in the range 0..len(str)-1 inclusive).
"""


def missing_char(str, n):
    str_list = []
    for i in range(len(str)):
        if i != n:
            str_list.append(str[i])

    return "".join(str_list)