#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 12.3


Создать функцию ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые передавны ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.

'''
from task_12_2 import check_ip_availability
from tabulate import tabulate
from pprint import pprint

def ip_table(good_ips,bad_ips):
    all_ips = {'Reachable':[],'Unreachable':[]}
    all_ips['Reachable'].extend(good_ips)
    all_ips['Unreachable'].extend(bad_ips)
    pprint(all_ips)
    print(tabulate(all_ips, headers='keys'))

if __name__ == "__main__":
    ip_list = ['8.8.8.8', '1.1.1.1-1.1.1.4', '100.3.3.3-5']
    good_ips, bad_ips = check_ip_availability(ip_list)
    ip_table(good_ips,bad_ips)
