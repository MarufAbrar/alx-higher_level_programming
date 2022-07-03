#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    '''function that deletes the item at a specific position in a list'''
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
    else:
        for i in range(len(my_list)):
            if i == idx:
                del my_list[i]
    return(my_list)
