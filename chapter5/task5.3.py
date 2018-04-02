#!/usr/bin/env python

access_template = ['switchport mode access',
'switchport access vlan {}',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
'switchport mode trunk',
'switchport trunk allowed vlan {}']


int_type = input('Enter interface mode(access/trunk):')
int_num = input('Enter interface type and number:')
int_vlans = input('Enter vlan(s):')

print('interface', int_num)

if int_type == 'access':
    print('\n'.join(access_template).format(int_vlans))
elif int_type == 'trunk':
    print('\n'.join(trunk_template).format(int_vlans))
else:
    print('Wrong interface type!')