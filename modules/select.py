#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def select(command_d, mans_list):
    parts = command_d.split(' ', maxsplit=1)
    sel = parts[1]
    count = 0
    for man in mans_list:
        if man.get('number') == sel:
            count += 1
            print(
                '{:>4}: {}'.format(count, man.get('name', ''))
            )
            print('Номер телефона:', man.get('number', ''))
            print('Дата рождения:', man.get('date', ''))

    # Если счетчик равен 0, то человек не найден.
    if count == 0:
        print("Человек не найден.")
