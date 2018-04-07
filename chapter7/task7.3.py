#!/usr/bin/env python

'''
CAM_table.txt

sw1#sh mac address-table 
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
 100    01bb.c580.7000    DYNAMIC     Gi0/1
 200    0a4b.c380.7000    DYNAMIC     Gi0/2
 300    a2ab.c5a0.7000    DYNAMIC     Gi0/3
 100    0a1b.1c80.7000    DYNAMIC     Gi0/4
 500    02b1.3c80.7000    DYNAMIC     Gi0/5
 200    1a4b.c580.7000    DYNAMIC     Gi0/6
 300    0a1b.5c80.7000    DYNAMIC     Gi0/7
'''

MACS = {}

with open('CAM_table.txt', 'r') as f:
    for line in f:
        if 'DYNAMIC' in line:
            vlan, mac, typ, ports = line.split()
            try:
                MACS[vlan].append({mac:ports})
            except KeyError:
                MACS[vlan] = [{mac:ports}]

#print(MACS)

for key in MACS.keys():
    #print(MACS[key])
    for mac in MACS[key]:
        for mackey in mac.keys():
            print(key, mackey, mac[mackey], sep='   ')