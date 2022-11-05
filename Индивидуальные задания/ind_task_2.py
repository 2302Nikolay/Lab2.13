#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from modules.mod_list import mod_list

mylist = list(map(int, input().split()))
a = int(input("Введите:\n 0, если хотите удалить чётные\n 1, если хотите удалить нечётные\n"))
print(mod_list(mylist)(a))
