#
# Copyright 2014 by Kurt Griffiths
#
# Creative Commons Attribution License (CC-BY)
#
#   http://creativecommons.org/licenses/by/3.0/
#


import hashlib
import os


def compress(data):
    return (hashlib.sha512(data).digest(), len(data))


def decompress(compressed):
    digest, length = compressed

    while True:
        data = os.urandom(length)
        if hashlib.sha512(data).digest() == digest:
            break

    return data
