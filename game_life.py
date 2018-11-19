#! /usr/bin/env python

import os
import pprint
import sys
import time
import random

max = 10

old, new = 0, 1
board = [0, 1]
board[old] = []
board[new] = []


for x in range(0,10):
    board[old].append([])
    board[new].append([])
    for y in range(0,10):
        board[old][x].append(0)
        board[new][x].append(0)

board[old][1][0] = 1
board[old][2][1] = 1
board[old][0][2] = 1
board[old][1][2] = 1
board[old][2][2] = 1

for  x in range(len(board[old])):
    for y in range(len(board[old][0])):
        print([x][y])


pp = pprint.PrettyPrinter()
pp.pprint(board)





