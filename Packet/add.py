#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import datetime


def add(list_man):
    # Запросить данные .
    name = input("Имя:  ")
    number = input("Номер телефона ")
    date = input("Дата рождения: ")
    date = datetime.datetime.strptime(date, '%d.%m.%Y').date()

    # Создать словарь.
    man = {
        'name': name,
        'number': number,
        'date': date,
    }

    # Добавить словарь в список.
    list_man.append(man)
    # Отсортировать список.
    if len(list_man) > 1:
        list_man.sort(key=lambda item: item.get('date', ''))
    return list_man
