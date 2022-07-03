#!/usr/bin/python3


def no_c(my_string):
    '''function that removes all characters c and C from a string'''
    result = ""
    for i in my_string:
        if i == 'c' or i == 'C':
            result += ""
        else:
            result += i
    return(result)
