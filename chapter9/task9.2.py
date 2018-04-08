#!/usr/bin/env python

from pprint import pprint

def generate_trunk_config(trunk):
    '''
    trunk - словарь trunk-портов для которых необходимо сгенерировать конфигурацию.
    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    '''
    trunk_template = [  'switchport trunk encapsulation dot1q',
                        'switchport mode trunk',
                        'switchport trunk native vlan 999',
                        'switchport trunk allowed vlan {}']
    
    conf = []

    for key,val in trunk.items():
        conf.append(' '.join(['interface',key]))
        vlans = ','.join(str(x) for x in val)
        for line in trunk_template:
            if 'allowed vlan' in line:
                conf.append(line.format(vlans))
            else:
                conf.append(line)
    
    return conf




trunk_dict = {  'FastEthernet0/1':[10,20,30],
                'FastEthernet0/2':[11,30],
                'FastEthernet0/4':[17] }


pprint (generate_trunk_config(trunk_dict))
