#!/usr/bin/env python

ip = input('Enter IP address:')

ip_first_octet = int(ip.split('.')[0])

if ip_first_octet in range(1,224):
    print('unicast')
elif ip_first_octet in range(224,240):
    print('multicast')
elif ip == '255.255.255.255':
    print('local broadcast')
elif ip == '0.0.0.0':
    print('unassigned')
else:
    print('unused')
