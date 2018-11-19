#!/usr/bin/python
# create head program myhead.py <count> <file>
import sys

f = open(sys.argv[2], "r")
count = int(sys.argv[1])
for w in f:
	if count > 0:
		print(w),
		count = count - 1
	else:
		break



