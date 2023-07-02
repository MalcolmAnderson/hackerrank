#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def compareTriplets(a, b):
    output = [0, 0]
    for x in range(3):
        print(f"x = {x}")
        print(f"a[{x}] = {a[x]}")
        print(f"b[{x}] = {b[x]}")
        print(a[x] > b[x], f"a{x} greater than b{x}")
        if a[x] > b[x]:
            output[0] += 1
        print(output)
        if b[x] > a[x]:
            output[1] += 1
        print(output)
    print(output)
    return output

    # Write your code here


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # a = list(map(int, input().rstrip().split()))

    # b = list(map(int, input().rstrip().split()))

    # result = compareTriplets(a, b)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()

    test = "1 7 8"
    a = list(map(int, test.rstrip().split()))
    print(a)

    # a = [1, 2, 3]
    b = [3, 2, 1]
    result = compareTriplets(a, b)
    print(result)
