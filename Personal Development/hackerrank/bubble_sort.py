#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#


def countSwaps(a):
    # Write your code here
    n = len(a)
    counter = 0
    for i in range(n):
        for j in range(n-1):
            if (a[j] > a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
                counter += 1

    string = f"Array is sorted in {counter} swaps." + \
        f"\nFirst Element: {a[0]}" + f"\nLast Element: {a[-1]}"
    print(string)


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
