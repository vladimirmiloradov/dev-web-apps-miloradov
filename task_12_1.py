"""
Задание 12.1
Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Функция ожидает как аргумент список IP-адресов.
Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов
Для проверки доступности IP-адреса, используйте команду ping.
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

import subprocess


def ping_ip_addresses(ip_addresses):
    reachable_ip = []
    unreachable_ip = []

    for ip in ip_addresses:
        result = subprocess.run(
            ["ping", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        if result.returncode == 0:
            reachable_ip.append(ip)
        else:
            unreachable_ip.append(ip)
    return reachable_ip, unreachable_ip


if __name__ == "__main__":
    print(ping_ip_addresses(["10.1.1.1", "192.168.1.1", "127.0.0.1", "255.255.255.255", "300.300.300.300"]))