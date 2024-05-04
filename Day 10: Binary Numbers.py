#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    data = bin(n)

    MAX = 0
    CURRENT = 0

for i in data:
    if i == '1':
        CURRENT = CURRENT + 1
    else:
        MAX = max(MAX, CURRENT)
        CURRENT = 0

print(max(MAX, CURRENT))
