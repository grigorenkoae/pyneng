#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 15.4a

Создать функцию convert_to_dict, которая ожидает два аргумента:
* список с названиями полей
* список кортежей с результатами отработки функции parse_sh_ip_int_br из задания 15.4

Функция возвращает результат в виде списка словарей (порядок полей может быть другой):
[{'interface': 'FastEthernet0/0', 'status': 'up', 'protocol': 'up', 'address': '10.0.1.1'},
 {'interface': 'FastEthernet0/1', 'status': 'up', 'protocol': 'up', 'address': '10.0.2.1'}]

Проверить работу функции на примере файла sh_ip_int_br_2.txt:
* первый аргумент - список headers
* второй аргумент - результат, который возвращает функции parse_show из прошлого задания.

Функцию parse_sh_ip_int_br не нужно копировать.
Надо импортировать или саму функцию, и использовать то же регулярное выражение,
что и в задании 15.4, или импортировать результат выполнения функции parse_show.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
import sys
from task_15_4 import parse_sh_ip_int_br
from pprint import pprint


headers = ['interface', 'address', 'status', 'protocol']


def convert_to_dict(headers,results):
    result = []
    for item in results:
        result.append(dict(zip(headers,item)))
    return result


if __name__ == "__main__":
    results = parse_sh_ip_int_br(sys.argv[1])
    result = convert_to_dict(headers,results)
    pprint(result)
