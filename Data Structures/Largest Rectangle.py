#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    res = 0

    for i in range(len(h)):
        length = 0
        for j in range(i, -1, -1):
            if h[j] >= h[i]:
                length += 1
            else:
                break

        for j in range(i + 1, len(h)):
            if h[j] >= h[i]:
                length += 1
            else:
                break

        res = max(res, length * h[i])

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
