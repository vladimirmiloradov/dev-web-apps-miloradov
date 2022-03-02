"""
Задание 5.2
Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24
Затем вывести информацию о сети и маске в таком формате:
Network:
10        1         1         0
00001010  00000001  00000001  00000000
Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000
Проверить работу скрипта на разных комбинациях сеть/маска.
Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)
Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def makeIPNetwork(ip, mask):
    ip[0] = str(int(ip[0], 10) & int(mask[0], 2))
    ip[1] = str(int(ip[1], 10) & int(mask[1], 2))
    ip[2] = str(int(ip[2], 10) & int(mask[2], 2))
    ip[3] = str(int(ip[3], 10) & int(mask[3], 2))
    return ip


def printIP(new_ip):
    upper_str = f'{new_ip[0]:<10}    {new_ip[1]:<10}    {new_ip[2]:<10}    {new_ip[3]:<10}'
    lower_str = '{:08b}      {:08b}      {:08b}      {:08b}'.format(
        int(new_ip[0]), int(new_ip[1]), int(new_ip[2]), int(new_ip[3]))
    result = f"""Network:
{upper_str} \n{lower_str}
"""
    return(result)
    

def printMask(mask_list, mask):
    upper_str = '{:<10}    {:<10}    {:<10}    {:<10}'.format(
        int(mask_list[0], 2), int(mask_list[1], 2), int(mask_list[2], 2), int(mask_list[3], 2))
    lower_str = f'{mask_list[0]:<10}    {mask_list[1]:<10}    {mask_list[2]:<10}    {mask_list[3]:<10}'
    result = f"""Mask: /{mask}
{upper_str} \n{lower_str}
"""
    return(result)


def makeMask(mask):
    mask_str = '1' * int(mask) + '0' * (32 - int(mask))
    oktet1 = mask_str[0:8]
    oktet2 = mask_str[8:16]
    oktet3 = mask_str[16:24]
    oktet4 = mask_str[24:32]
    mask_list = [oktet1, oktet2, oktet3, oktet4]
    return mask_list

ip_address = input('Введите ip/mask: ').split('/')
ip = ip_address[0]
mask = ip_address[1]
mask_res = makeMask(mask)
ip_res = ip.split('.')
ip_to_str = printIP(ip_res)
mask_to_str = printMask(mask_res, mask)
print(ip_to_str + mask_to_str)
