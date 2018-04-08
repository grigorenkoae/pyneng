#!/usr/bin/env python

from pprint import pprint

ignore = ['duplex', 'alias', 'Current configuration', 'end']

def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.
    command - строка. Команда, которую надо проверить
    ignore - список. Список слов
    Возвращает True, если в команде содержится слово из списка ignore, False - если нет
    '''
    return any(word in command for word in ignore)


def parse_config(file):

    conf = {}

    with open(file,'r') as f:
        for line in f:
            if ignore_command(line,ignore) or line.startswith('!'):
               pass
            else:
                if not line.startswith(' '):
                    key = line.strip()
                    conf[key] = []
                elif line.startswith(' ') and not line.startswith('  '):
                    line2 = line.strip()
                    conf[key] = {line2:[]}
                elif line.startswith('  '):
                    conf[key][line2].append(line.strip())

    
    return conf


pprint(parse_config('config_r1.txt'))
