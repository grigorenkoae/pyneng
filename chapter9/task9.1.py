#!/usr/bin/env python

from pprint import pprint

def generate_access_config(access):
    '''
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
        'FastEthernet0/14':11,
        'FastEthernet0/16':17}

    Возвращает список всех портов в режиме access
    с конфигурацией на основе шаблона
    '''
    access_template = [ 'switchport mode access',
                        'switchport access vlan {}',
                        'switchport nonegotiate',
                        'spanning-tree portfast',
                        'spanning-tree bpduguard enable']
    
    conf = []

    for key,val in access.items():
        conf.append(' '.join(['interface',key]))
        for line in access_template:
            if 'vlan' in line:
                conf.append(line.format(val))
            else:
                conf.append(line)
    
    return conf


access_dict = { 'FastEthernet0/12':10,
'FastEthernet0/14':11,
'FastEthernet0/16':17,
'FastEthernet0/17':150 }


pprint (generate_access_config(access_dict))
