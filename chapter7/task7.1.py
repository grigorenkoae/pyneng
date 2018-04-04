#!/usr/bin/env python

template = '''
Protocol: {0}
Prefix: {1}
AD/Metric: {2}
Next-Hop: {3}
Last update: {4}
Outbound Interface: {5}
'''

with open('task7.1.txt','r') as f:
    for line in f:
        print(template.format(line.split()[0], line.split()[1], line.split()[2].replace('[','').replace(']',''), line.split()[4].replace(',',''), line.split()[5].replace(',',''), line.split()[6]))


