"""
Задание 7.1
Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def infoIp(ospf_route):
    list1 = ospf_route.split()
    result = {'Prefix': list1[1], 'AD/Metric': list1[2].strip('[]'), 'via': list1[3], 'Next-Hop': list1[4].strip(','),
              'Last update': list1[5].strip(','), 'Outbound Interface': list1[6]}
    template = """ 
    Prefix              {} 
    AD/Metric           {} 
    Next-Hop            {} 
    Last update         {} 
    Outbound Interface  {} 
    """
    del result['via']
    result_str = template.format(result['Prefix'], result['AD/Metric'],
                                 result['Next-Hop'], result['Last update'], result['Outbound Interface'])
    return result_str


file = open('ospf.txt', 'r')
for string in file:
    print(infoIp(string))
file.close()