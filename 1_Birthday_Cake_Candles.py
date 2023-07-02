#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#


def birthdayCakeCandles(candles):
    candles.sort()
    max_value = max(candles)
    max_start = candles.index(max_value)
    max_count = len(candles) - max_start
    return max_count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # candles_count = int(input().strip())

    # candles = list(map(int, input().rstrip().split()))

    candles = [4, 4, 1, 3]
    result = birthdayCakeCandles(candles)

    # fptr.write(str(result) + '\n')

    # fptr.close()
    print(result)
