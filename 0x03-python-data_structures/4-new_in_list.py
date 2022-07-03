#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    '''function that replaces an element in a list at
    a specific position without modifying the original list'''
    new_list = []
    for i in range(0, len(my_list)):
        new_list.append(my_list[i])
    if idx >= 0 and idx < len(my_list):
        new_list[idx] = element
    return (new_list)
