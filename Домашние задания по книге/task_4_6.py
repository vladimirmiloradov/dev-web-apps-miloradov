"""
Задание 4.6
Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0
Ограничение: Все задания надо выполнять используя только пройденные темы.
Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
split_route = ospf_route.split()
collection = {'Prefix': split_route[0], 'AD/Metric': split_route[1].strip('[]'), 'via': split_route[2], 'Next-Hop': split_route[3].strip(','),
            'Last update': split_route[4].strip(','), 'Outbound Interface': split_route[5]}
template = """ 
Prefix              {} 
AD/Metric           {} 
Next-Hop            {} 
Last update         {} 
Outbound Interface  {} 
"""
del collection['via']
result = template.format(collection['Prefix'], collection['AD/Metric'],
                                collection['Next-Hop'], collection['Last update'], collection['Outbound Interface'])
print(result)