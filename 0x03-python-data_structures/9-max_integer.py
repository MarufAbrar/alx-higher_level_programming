#!/usr/bin/python3


def max_integer(my_list=[]):
    '''function that finds the biggest integer of a list'''
    if len(my_list) == 0:
        return (None)
    biggest = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > biggest:
            biggest = my_list[i]
    return (biggest)
