#!/usr/bin/python3
for ASCII_alphabet in range(97, 123):
    if chr(ASCII_alphabet) != 'e' and chr(ASCII_alphabet) != 'q':
        print("{}".format(chr(ASCII_alphabet)), end="")
