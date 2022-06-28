The ``Say My Name`` module
==========================

Using ``say_my_name``
---------------------

First import ``say_my_name`` from the ``Say My Name`` module:

    >>> say_my_name = __import__("3-say_my_name").say_my_name

Now use it:

    >>> say_my_name("John", "Smith")
    My name is John Smith

    >>> say_my_name("Bob")
    My name is Bob 

    >>> say_my_name("Bob", 12)
    Traceback (most recent call last):
    TypeError: last_name must be a string

    >>> say_my_name("")
    My name is  

    >>> say_my_name(1)
    Traceback (most recent call last):
    TypeError: first_name must be a string

    >>> say_my_name(1, "Ross")
    Traceback (most recent call last):
    TypeError: first_name must be a string

    >>> say_my_name()
    Traceback (most recent call last):
    TypeError: say_my_name() missing 1 required positional argument: 'first_name'

    >>> say_my_name("Ace", "of Spades")
    My name is Ace of Spades

    >>> say_my_name([], 10)
    Traceback (most recent call last):
    TypeError: first_name must be a string

    >>> say_my_name("string", None)
    Traceback (most recent call last):
    TypeError: last_name must be a string

    >>> say_my_name("arg1", "arg2", "arg3")
    Traceback (most recent call last):
    TypeError: say_my_name() takes from 1 to 2 positional arguments but 3 were given
