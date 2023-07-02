#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# Reduce a string of lowercase characters in range ascii[‘a’..’z’]by doing a series of operations. In each operation, select a pair of adjacent letters that match, and delete them.

# Delete as many characters as possible using this method and return the resulting string. If the final string is empty, return Empty String


def reduceString(s):
    print("reduceString - Begin")
    result = ""
    len_s = len(s)
    i = 0
    while i < len_s:
        current_letter = s[i]
        if i+1 < len_s:
            next_letter = s[i+1]
            if next_letter == current_letter:
                i = i+2
            else:
                result += current_letter
                i = i+1
        else:
            result += current_letter
            i = i+1

    if result == "":
        result = "Empty String"
    print("reduceString - End")
    return result


def superReducedString(s):
    print("superReducedString - Begin")
    old_len = len(s)
    result = reduceString(s)
    new_len = len(result)
    if result == "Empty String":
        return result
    else:
        while old_len != new_len:
            old_len = new_len
            result = reduceString(result)
            if result == "Empty String":
                print("superReducedString - End Empty")
                return result
            new_len = len(result)
    print("superReducedString - End Normal")
    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = "aaabccddd"
    # result = superReducedString(s)
    # if result == "abd":
    #     print("PASS")
    # else:
    #     print(f"FAIL - returned {result}, but expected abd")

    s = "baab"
    result = superReducedString(s)
    if result == "Empty String":
        print("PASS")
    else:
        print(f"FAIL - returned {result}, but expected Empty String")
