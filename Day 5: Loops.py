#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    result=1
    n = int(input().strip())
    for i in range(1,11):
        result=n*i
        print(f"{n} x {i} = {n * i}")
