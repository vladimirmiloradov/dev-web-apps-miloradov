"""
Задание 6.2a
Сделать копию скрипта задания 6.2.
Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255
Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


ip = input('Введите ip: ')
oktet_list = ip.split('.')
flag = True
if len(oktet_list) == 4:
   for oktet in oktet_list:
      if not (oktet.isdigit() and 0 <= int(oktet) <= 255):
         flag = False
         break
else:
   flag = False
if flag:
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
else:
   print('Неправильный IP-адрес')

