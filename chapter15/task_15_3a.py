#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 15.3a

Переделать функцию parse_cfg из задания 15.3 таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

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
                result[interface] = ip_regex.search(line).groups()
    
    return result


if __name__ == "__main__":
    pprint(parse_cfg(sys.argv[1]))
