#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_items = set(my_list)
    result = 0
    for n in uniq_items:
        result += n
    return result
