#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    for i in range(1, n+1):
        out = ""
        is_string = False
        if i % 3 == 0:
            out += "Fizz"
            is_string = True
        if i % 5 == 0:
            out += "Buzz"
            is_string = True
        if is_string:
            print(out)
        else:
            print(i)


if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
