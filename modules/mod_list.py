#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def mod_list(lst):
    def mod_list_1(typ):
        if typ == 1:
            for i in lst:
                if i % 2 > 0:
                    lst.remove(i)
        elif typ == 0:
            for i in lst:
                if i % 2 == 0:
                    lst.remove(i)
        return lst
    return mod_list_1
