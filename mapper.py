#!/usr/bin/env python

import sys

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    #split the line into words
    word = line.split('|')[3]
    #increase counters
    #for word in words:
        #write the results to STDOUT
        #what is outputted here will be the input for the
        #reduce step, i.e. the input for reducer.py
        #
        # tab delimited; the trivial word count is 1
    print '%s\t%s' % (word, 1)
