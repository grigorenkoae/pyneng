#!/usr/bin/env python

mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
mac_cisco = []

for address in mac:
    address_cisco = address.replace(':','.')
    mac_cisco.append(address_cisco)

print(mac_cisco)