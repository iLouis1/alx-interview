#!/usr/bin/python3
"""The UTF-8 Validation"""


def validUTF8(data):
    """
    data: List of integers
    Return: True if data is a valid UTF-8
    encoding, else return False
    """
    byte_count = 0

    for k in data:
        if byte_count == 0:
            if k >> 5 == 0b110 or k >> 5 == 0b1110:
                byte_count = 1
            elif k >> 4 == 0b1110:
                byte_count = 2
            elif k >> 3 == 0b11110:
                byte_count = 3
            elif k >> 7 == 0b1:
                return False
        else:
            if k >> 6 != 0b10:
                return False
            byte_count -= 1

    return byte_count == 0
