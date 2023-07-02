#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    stem = s[2:len(s)-2]
    am_pm = s[len(s)-2]
    hour_string = s[0:2]
    hour_int = int(hour_string)
    if hour_string == "12" and am_pm == "A":
        hour_string = "00"
    if hour_int < 12 and am_pm == "P":
        hour_int += 12
        hour_string = str(hour_int).zfill(2)
    return f"{hour_string}{stem}"
    # print(f"{hour_string}{stem}    - {s}")


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    print(timeConversion("12:01:00PM"))
    print(timeConversion("12:01:00AM"))
    print(timeConversion("02:01:00AM"))
    print(timeConversion("02:01:00PM"))

    # fptr.write(result + '\n')

    # fptr.close()
