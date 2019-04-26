#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
n = int(input())

c = list(map(int, input().rstrip().split()))
#print(len(c))
# cloud_safe =  0
# cloud_unsafe = 1
#count = 0
jumps = 0
i = 0
#ab = len(c)-1
#print(ab)

#for i in range(len(c)):
while i < len(c)-1:
    if i+2 < len(c) and c[i+2] == 0:
        i = i + 2
        
    else:
        i = i + 1
    jumps += 1  
print(jumps)
