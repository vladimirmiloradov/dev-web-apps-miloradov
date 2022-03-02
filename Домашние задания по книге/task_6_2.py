"""
Задание 6.2
Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input('Введите ip: ')
oktet_list = ip.split('.')
oktet_1 = int(oktet_list[0])
if 1 <= oktet_1 <= 223:
   print('unicast')
elif 224 <= oktet_1 <= 239:
   print('multicast')
elif ip == '255.255.255.255':
   print('local broadcast')
elif ip == '0.0.0.0':
   print('unassigned')
else:
   print('unused')