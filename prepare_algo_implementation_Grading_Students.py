# HackerLand University has the following grading policy:

# Every student receives a  in the inclusive range from  to .
# Any  less than  is a failing grade.
# Sam is a professor at the university and likes to round each student's  according to these rules:

# If the difference between the  and the next multiple of  is less than , round  up to the next multiple of .
# If the value of  is less than , no rounding occurs as the result will still be a failing grade.
# Examples

#  round to  (85 - 84 is less than 3)
#  do not round (result is less than 40)
#  do not round (60 - 57 is 3 or higher)
# Given the initial value of  for each of Sam's  students, write code to automate the rounding process.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def gradingStudents(grades):
    # Write your code here
    results = []
    for grade in grades:
        grade_mod_5 = grade % 5
        if grade > 35 and grade_mod_5 >= 3:
            grade += 5 - grade_mod_5
        results.append(grade)
    return results


if __name__ == '__main__':
    expected = [75, 67, 40, 33]
    test = expected

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades = [73, 67, 38, 33]
    expected = [75, 67, 40, 33]

    result = gradingStudents(grades)

    print(f"73 mod 5 = {73%5}")

    print(f"expected = {expected}")
    print(f"actual   = {result}")
