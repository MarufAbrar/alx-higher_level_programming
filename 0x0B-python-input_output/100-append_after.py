#!/usr/bin/python3
"""append after module"""


def append_after(filename="", search_string="", new_string=""):
    """append a text after a substring line"""

    with open(filename, 'r') as f:
        content = f.readlines()
        for (index, line) in enumerate(content):
            if line.find(search_string) != -1:
                content.insert(index+1, new_string)
        new_content = "".join(content)
    f = open(filename, 'w')
    f.write(new_content)
    f.close()
