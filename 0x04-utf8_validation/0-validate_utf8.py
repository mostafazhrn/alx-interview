#!/usr/bin/python3
""" THis script shall validate data to determine is valid UTF-8 encoding"""


def validUTF8(data):
    """ THis instance shall validate given data ro check utf encoding"""
    try:
        mask_donne = [x & 255 for x in data]
        bytes(mask_donne).decode("UTF-8")
        return True
    except UnicodeError:
        return False
