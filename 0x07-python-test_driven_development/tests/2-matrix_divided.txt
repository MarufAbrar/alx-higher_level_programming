The "2-matrix_divided" module
==========================

Using "matrix_divided"
-------------------

Import file:
>>> matrix_divided = __import__('2-matrix_divided').matrix_divided

>>> matrix_divided([[1, 2, 3], [4, 5, 6]], 0)
Traceback (most recent call last):
ZeroDivisionError: division by zero

>>> matrix_divided([[1, 2, 3], [1.67, 5, 6]], 3)
[[0.33, 0.67, 1.0], [0.56, 1.67, 2.0]]

>>> matrix_divided([[1, 2, 3], [4, 5, 6]], "holberton")
Traceback (most recent call last):
TypeError: div must be a number

>>> matrix_divided([["a", "b", "c"], [4, 5, 6]], 3)
Traceback (most recent call last):
TypeError: matrix must be a matrix (list of lists) of integers/floats

>>> matrix_divided([[1, 4, 2, 3, 10], [3, 2, 6]], 2)
Traceback (most recent call last):
TypeError: Each row of the matrix must have the same size

>>> matrix_divided([[], [4, 5, 6]], 2)
Traceback (most recent call last):
TypeError: Each row of the matrix must have the same size

>>> matrix_divided([[3, 9], [12, 15]], -3)
[[-1.0, -3.0], [-4.0, -5.0]]
