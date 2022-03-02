"""
Задание 5.2a
Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску,
как в задании 5.2.
Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16
Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28
Если пользователь ввел адрес 10.0.1.1/24, вывод должен быть таким:
Network:
10        0         1         0
00001010  00000000  00000001  00000000
Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000
Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24
Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)
Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит
адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28 в двоичном формате будет
bin_ip = "00001010000000010000000111000011"
А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего
в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def makeIPNetwork(ip, mask):
    ip[0] = str(int(ip[0], 10) & int(mask[1], 2))
    ip[1] = str(int(ip[1], 10) & int(mask[2], 2))
    ip[2] = str(int(ip[2], 10) & int(mask[3], 2))
    ip[3] = str(int(ip[3], 10) & int(mask[4], 2))
    return ip


def printIP(new_ip):
    upper_str = f'{new_ip[0]:<10}    {new_ip[1]:<10}    {new_ip[2]:<10}    {new_ip[3]:<10}'
    lower_str = '{:08b}      {:08b}      {:08b}      {:08b}'.format(
        int(new_ip[0]), int(new_ip[1]), int(new_ip[2]), int(new_ip[3]))
    result = f"""Network:
{upper_str} \n{lower_str}
"""
    return(result)
    

def printMask(mask_list):
    upper_str = '{:<10}    {:<10}    {:<10}    {:<10}'.format(
        int(mask_list[1], 2), int(mask_list[2], 2), int(mask_list[3], 2), int(mask_list[4], 2))
    lower_str = f'{mask_list[1]:<10}    {mask_list[2]:<10}    {mask_list[3]:<10}    {mask_list[4]:<10}'
    result = f"""
Mask:
/{mask_list[0]}
\n{upper_str}\n{lower_str}
"""
    return(result)


def makeMask(mask):
    mask_str = '1' * int(mask) + '0' * (32 - int(mask))
    mask_int = mask
    oktet1 = mask_str[0:8]
    oktet2 = mask_str[8:16]
    oktet3 = mask_str[16:24]
    oktet4 = mask_str[24:32]
    mask_list = [mask_int, oktet1, oktet2, oktet3, oktet4]
    return mask_list


ip_address = input('Введите ip/mask: ').split('/')
ip = ip_address[0]
mask = ip_address[1]
mask_res = makeMask(mask)
ip_res = makeIPNetwork(ip.split('.'), mask_res)
ip_to_str = printIP(ip_res)
mask_to_str = printMask(mask_res)
print(ip_to_str + mask_to_str)
