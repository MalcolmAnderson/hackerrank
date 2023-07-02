#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#


def staircase(n):
    for i in range(1, n+1):
        spaces = " " * (n-i)
        octothorpes = "#" * (i)
        print(spaces + octothorpes)
    # Write your code here


if __name__ == '__main__':
    # n = int(input().strip())
    n = 5
    staircase(n)
