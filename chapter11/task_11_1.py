#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.

Проверить работу функции на содержимом файла sw1_sh_cdp_neighbors.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

from pprint import pprint

def parse_cdp_neighbors(string):

    CDP = {}
    n = 0

    for line in string.split('\n'):
        if 'show cdp neighbors' in line:
            hostname = line.split('>')[0]
        if line == '':
            n = 0
        if 'Device ID' in line:
            n = 1
            continue
        if n == 1:
            remote_device = line.split()[0]
            local_port = ''.join(line.split()[1:3])
            remote_port = ''.join(line.split()[-2:])
            if hostname > remote_device:
                CDP[(hostname,local_port)] = (remote_device,remote_port)
            else:
                CDP[(remote_device,remote_port)] = (hostname,local_port)
    
    return CDP


if __name__ == "__main__":
    with open('sw1_sh_cdp_neighbors.txt','r') as f:
        data = f.read()
        pprint(parse_cdp_neighbors(data))
