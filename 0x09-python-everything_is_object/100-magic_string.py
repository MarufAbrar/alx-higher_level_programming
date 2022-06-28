#!/usr/bin/python3


def call_counter(func):
    def helper():
        helper.calls += 1
        return func()
    helper.calls = 0

    return helper


@call_counter
def magic_string():
    return 'Holberton, ' * (magic_string.calls - 1) + 'Holberton'
