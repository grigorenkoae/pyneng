#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 15.3b

Проверить работу функции parse_cfg из задания 15.3a на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция parse_cfg, интерфейсу Ethernet0/1
соответствует только один из них (второй).

Переделайте функцию parse_cfg из задания 15.3a таким образом,
чтобы она возвращала список кортежей для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет несколько кортежей.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''
import sys
import re
from pprint import pprint


def parse_cfg(file):

    int_regex = re.compile(r'^interface (\S*)')
    ip_regex = re.compile(r'.*ip address ((?:\d{1,3}.){3}\d{1,3}) ((?:\d{1,3}.){3}\d{1,3})')
    result = {}

    with open(file) as f:

        for line in f:
            if int_regex.search(line):
                interface = int_regex.search(line).group()
            if ip_regex.search(line):
                try:
                    result[interface].append(ip_regex.search(line).groups())
                except KeyError:
                    result[interface] = [(ip_regex.search(line).groups())]
    
    return result


if __name__ == "__main__":
    pprint(parse_cfg(sys.argv[1]))
