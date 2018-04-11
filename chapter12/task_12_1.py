#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию check_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.
И возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.
Адрес считается доступным, если на три ICMP-запроса пришли три ответа.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
import subprocess

def ping_ip(ip_address):
    """
    Ping IP address and return tuple:
    On success:
        * True
        * command output (stdout)
    On failure:
        * False
        * error output (stderr)
    """
    print('Checking ip address {}'.format(ip_address))
    reply = subprocess.run(['ping', '-c', '3', '-n', ip_address],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            encoding='utf-8')
    if reply.returncode == 0:
        print('IP {} is alive'.format(ip_address))
        return True, reply.stdout
    else:
        print('IP {} not responding'.format(ip_address))
        return False, reply.stderr

#print(ping_ip('8.8.8.8'))


def check_ip_addresses(ip_list):
    good_ip_list = []
    bad_ip_list = []
    
    for ip in ip_list:
        if ping_ip(ip)[0]:
            good_ip_list.append(ip)
        else:
            bad_ip_list.append(ip)
    
    return good_ip_list, bad_ip_list


if __name__ == "__main__":
    list_of_ips = ['8.8.8.8', '1.1.1.1', '192.168.0.1', 'a']
    good_ips, bad_ips = check_ip_addresses(list_of_ips)
    print('good ip list: {} \nbad ip list: {}'.format(good_ips,bad_ips))
