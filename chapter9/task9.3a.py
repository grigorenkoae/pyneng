#!/usr/bin/env python

from pprint import pprint

def get_int_vlan_map(file):

    access_ports = {}
    trunk_ports = {}
    
    with open(file,'r') as f:
        for line in f:
            if line.startswith('interface '):
                int_name = line.split()[1]
            if line.startswith(' switchport trunk allowed vlan '):
                access_flag = False
                access_vlan_flag = False
                int_trunk_vlans = (line.split()[-1]).split(',')
                trunk_ports[int_name] = int_trunk_vlans

            if line.startswith(' switchport mode access'):
                access_flag = True
            if line.startswith(' switchport access vlan '):
                access_vlan_flag = True
                int_acc_vlan = line.split()[-1]
                access_ports[int_name] = int_acc_vlan
            if line.startswith(' duplex auto') and access_flag and not access_vlan_flag:
                int_acc_vlan = 1
                access_ports[int_name] = int_acc_vlan

    return access_ports, trunk_ports

pprint(get_int_vlan_map('config_sw2.txt'))
            