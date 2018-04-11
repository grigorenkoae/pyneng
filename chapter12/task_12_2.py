#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 12.2


Функция check_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например,
192.168.100.1-10.

Создать функцию check_ip_availability, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

IP-адреса могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо проверить доступность всех адресов диапазона включая последний.

Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.

Функция возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задачи можно воспользоваться функцией check_ip_addresses из задания 12.1
'''

from task_12_1 import check_ip_addresses
import ipaddress


def ip_range_to_ip_list(ip_list):
    final_ip_list = []
    for ip_string in ip_list:
        if '-' in ip_string:
            first_ip, last_ip = ip_string.split('-')
            first_ip_last_octet = first_ip.split('.')[-1]

            if '.' in last_ip:
                last_octet = last_ip.split('.')[-1]
            else:
                last_octet = last_ip

            first_ip_addr = ipaddress.ip_address(first_ip)

            for i in range(0, int(last_octet)+1-int(first_ip_last_octet)):
                final_ip_list.append(str(first_ip_addr+i))
        else:
            final_ip_list.append(ip_string)
    
    return final_ip_list


def check_ip_availability(ip_list):
    final_ip_list = ip_range_to_ip_list(ip_list)
    good_ips, bad_ips = check_ip_addresses(final_ip_list)

    return good_ips, bad_ips


if __name__ == "__main__":
    ip_list = ['8.8.8.8', '1.1.1.1-1.1.1.4', '100.3.3.3-5']
    good_ips, bad_ips = check_ip_availability(ip_list)
    print('good ip list: {} \nbad ip list: {}'.format(good_ips,bad_ips))
