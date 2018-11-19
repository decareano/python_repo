#!/usr/bin/env python

import time
import random
import os



input_file = open("grid.txt", 'r')
for line in input_file:
            temp = []
            print(line)
for i in range(len(line) - 1):
    if line[i] == "*":
            print(line[i])
            temp.append(1)
    elif line[i] == ".":
            temp.append(0)
