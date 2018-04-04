#!/usr/bin/env python

import sys

ignore = ['duplex', 'alias', 'Current configuration']

with open(sys.argv[1],'r') as f:
    for line in f:
        if not line.startswith('!'):
            for ignored_word in ignore:
                if ignored_word in line:
                    break
            else:
                print(line.rstrip())

