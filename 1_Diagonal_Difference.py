#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    # assume 2d square array
    size = len(arr[0])
    # get diaganal down
    dd = 0
    for x in range(size):
        dd += arr[x][x]
    print(f"dd = {dd}")
    du = 0
    for x in range(size):
        du += arr[size-1-x][x]
    print(f"du = {du}")
    output = abs(dd-du)
    return output

    # Write your code here


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # arr = []

    # for _ in range(n):
    #     arr.append(list(map(int, input().rstrip().split())))

    # result = diagonalDifference(arr)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    #   3   5   9
    #   7   10  2
    #   -3  12  6
    # diff = 3

    arr = [[3, 5, 9], [7, 10, 2], [-3, 12, 6]]
    output = diagonalDifference(arr)
    print(output)
