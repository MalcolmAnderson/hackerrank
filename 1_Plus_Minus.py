#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    size_of_array = len(arr)
    count_pos = 0
    count_neg = 0
    count_zero = 0
    for x in arr:
        if x > 0:
            count_pos += 1
        if x == 0:
            count_zero += 1
        if x < 0:
            count_neg += 1
    print(f"{count_pos/size_of_array:.6f}")
    print(f"{count_neg/size_of_array:.6f}")
    print(f"{count_zero/size_of_array:.6f}")

    # Write your code here


if __name__ == '__main__':
    # n = int(input().strip())

    # arr = list(map(int, input().rstrip().split()))

    arr = [1, 1, 0, -1, -1]
    plusMinus(arr)
