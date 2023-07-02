#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def camelcase(s):
    wordCount = 1
    # assumes first letter is lower case and is the beginning of word 1
    for i in range(1, len(s)):
        if s[i].isupper():
            wordCount += 1
    return wordCount


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()
    s = "saveChangesInTheEditor"

    result = camelcase(s)

    if result == 5:
        print("PASS")
    else:
        print(f"FAIL - returned {result}, but expected 5")

    # fptr.write(str(result) + '\n')

    # fptr.close()
