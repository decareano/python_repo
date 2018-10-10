#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    a_triplet = map(int, input().split())  
    b_triplet = map(int, input().split())
    alice_points = 0
    bob_points = 0
    for a_val, b_val in zip(a_triplet, b_triplet):
        if a_val < b_val:
            bob_points += 1
        elif a_val > b_val:
            alice_points += 1
result = compareTriplets(a, b)
