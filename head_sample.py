#!/usr/bin/env 
import sys

def head(filename, count=1):
    """
    This one is fairly trivial to implement but it is here for completeness.
    """
    with open(filename, 'r') as f:
        lines = [f.readline() for line in xrange(1, count+1)]
        return filter(len, lines)