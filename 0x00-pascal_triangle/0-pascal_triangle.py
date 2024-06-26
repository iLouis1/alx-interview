#!/usr/bin/python3
"""The Pascal Triangle Interview Challenge"""


def pascal_triangle(n):
    """returns a list of lists of numbers
    representing the pascal triangle"""
    if n <= 0:
        return []

    pascal_triangle = [0] * n

    for k in range(n):
        # define a row and fill first and last idx with 1
        new_row = [0] * (k+1)
        new_row[0] = 1
        new_row[len(new_row) - 1] = 1

        for y in range(1, k):
            if y > 0 and y < len(new_row):
                a = pascal_triangle[k - 1][y]
                b = pascal_triangle[k - 1][y - 1]
                new_row[y] = a + b

        pascal_triangle[k] = new_row

    return pascal_triangle
