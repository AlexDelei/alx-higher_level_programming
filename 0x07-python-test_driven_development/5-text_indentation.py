#!/usr/bin/python3
"""
Module for printing text
"""


def text_indentation(text):
    """
    Text printing regarding special marks

    Parameters:
    text(str) - the text


    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    newline_printed = False

    for char in text:
        if char == ' ':
            if not newline_printed:
                print('', end='')
                newline_printed = True
            continue
        print(char, end='')
        if char in ['.', '?', ':']:
            print('\n\n', end='')
            newline_printed = True
    print()


if __name__ == "__main__":
    import doctest
    doctest.testmod("./tests/5-text_indentation.txt")
