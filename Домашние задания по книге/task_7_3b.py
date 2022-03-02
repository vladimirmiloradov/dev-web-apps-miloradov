"""
Задание 7.3b
Сделать копию скрипта задания 7.3a.
Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.
Пример работы скрипта:
Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

num_vlan = input('Enter VLAN number: ')
with open('CAM_table.txt') as file:
    for string in file:
        arr = string.split()
        if arr and arr[0].isdigit() and arr[0] == num_vlan:
            vlan, mac, dyn, intf = arr
            print(f'{vlan:<10}{mac:20}{intf}')
