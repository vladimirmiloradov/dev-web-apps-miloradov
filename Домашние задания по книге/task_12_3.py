"""
Задание 12.3
Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.
Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов
Результат работы функции - вывод на стандартный поток вывода таблицы вида:
Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9
"""

from tabulate import tabulate


def print_ip_table(reachable_ip, unreachable_ip):
    table = {"Reachable": reachable_ip, "Unreachable": unreachable_ip}
    print(tabulate(table, headers="keys"))


if __name__ == "__main__":
    reachable_ip = ["10.1.1.1", "10.1.1.2"]
    unreachable_ip = ["10.1.1.7", "10.1.1.8", "10.1.1.9"]
    print_ip_table(reachable_ip, unreachable_ip)