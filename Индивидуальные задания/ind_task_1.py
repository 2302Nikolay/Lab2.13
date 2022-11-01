#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
import sys
from modul import add, select, list_d, help_d
if __name__ == '__main__':
    manlist = []
    while True:
        # Запросить команду
        command = input(">>> ").lower()
        if command == 'exit':
            break
        elif command == 'add':
            manlist = add(manlist)
        elif command == 'list':
            list_d(manlist)
        elif command.startswith('select '):
            select(command, manlist)
        elif command == 'help':
            help_d()
        else:
            print("неизвестная команда {command}", file=sys.stderr)
