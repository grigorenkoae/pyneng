# -*- coding: utf-8 -*-
'''
Задание 17.2c

С помощью функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует описанию в файле topology.yaml

Обратите внимание на то, какой формат данных ожидает функция draw_topology.
Описание топологии из файла topology.yaml нужно преобразовать соответствующим образом,
чтобы использовать функцию draw_topology.

Для решения задания можно создать любые вспомогательные функции.

Не копировать код функции draw_topology.

В итоге, должно быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_10_2c_topology.svg

При этом:
* Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''
from draw_network_graph import draw_topology
import yaml
from pprint import pprint


with open('topology.yaml') as f:
    topology = yaml.load(f)
#pprint(topology)


new_topology = {}
for hostname,val in topology.items():
    for local_int, val1 in val.items():
        for remote_name,remote_port in val1.items():
            if hostname > remote_name:
                new_topology.update({(hostname,local_int):(remote_name,remote_port)})
            else:
                new_topology.update({(remote_name,remote_port):(hostname,local_int)})
pprint(new_topology)


draw_topology(new_topology)