#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 15.4

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'up', 'up')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br_2.txt.
FastEthernet0/1            10.0.12.1       YES manual up                    up
FastEthernet0/2            10.0.13.1       YES manual up                    up
FastEthernet0/3            unassigned      YES unset  administratively down down
Loopback0                  10.1.1.1        YES manual up                    up
Loopback100                100.0.0.1       YES manual up                    up

'''
import sys
import re
from pprint import pprint

def parse_sh_ip_int_br(file):
    regex = re.compile(r'(\S+) +(\S+) +\S+ +\S+ +(up|down|administratively down) +(up|down)')
    result = []
    with open(file) as f:
        for line in f:
            if regex.search(line):
                result.append(regex.search(line).groups())
    return result

if __name__ == "__main__":
    pprint(parse_sh_ip_int_br(sys.argv[1]))
