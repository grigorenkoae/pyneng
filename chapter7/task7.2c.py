#!/usr/bin/env python

import sys

ignore = ['duplex', 'alias', 'Current configuration']

with open(sys.argv[1],'r') as f, open(sys.argv[2],'w') as w:
    for line in f:
        for ignored_word in ignore:
            if ignored_word in line:
                break
        else:
            w.write(line)

