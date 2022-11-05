#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def list_d(list_man):
    if list_man:
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 20
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                "No",
                "Имя",
                "Номер телефона",
                "Дата рождения"
            )
        )
        print(line)

        # Вывести данные о человеке.
        for idx, man in enumerate(list_man, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:<20}  |'.format(
                    idx,
                    man.get('name', ''),
                    man.get('number', ''),
                    man.get('date', '')
                )
            )

        print(line)
    else:
        print("Список работников пуст: ")
