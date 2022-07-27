#!/usr/bin/python3
"""
File: 5-text_indentation.py

By: Maruf Abrar <maracode1@gmail.com>

Defines function that prints a text with 
2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines 
    after each of these characters: ., ? and :

    Args:
        text (str): text input
    Raises:
        TypeError: if text is not a string
    There should be no space at the beginning 
    or at the end of each printed line
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
