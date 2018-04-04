#!/usr/bin/env python

while True:
    ip = input('Enter IP address:')

    try:
        ip_first_octet = int(ip.split('.')[0])
        ip_second_octet = int(ip.split('.')[1])
        ip_third_octet = int(ip.split('.')[2])
        ip_forth_octet = int(ip.split('.')[3])
        if ip_first_octet in range(0,256) and ip_second_octet in range(0,256) and ip_third_octet in range(0,256) and ip_forth_octet in range(0,256) and len(ip.split('.')) == 4:
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
            break
        else:
            print('Incorrect IPv4 address')
    except (ValueError, IndexError):
        print('Incorrect IPv4 address')
    
