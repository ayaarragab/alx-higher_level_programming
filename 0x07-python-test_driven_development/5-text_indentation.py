#!/usr/bin/python3
'''
this module contains a function that prints a
text with 2 new lines
after each of these characters: ., ? and :
'''


def text_indentation(text):
    """
    text_indentation(text): for each (., :, ?) => 2 newlines
    """

    newText = ""
    in_whitespace = False   # tracker for whitespace after the (., ?, :)
    if text is None or not isinstance(text, str):
        raise TypeError('text must be a string')
    for c in text:
        if c == '.' or c == '?' or c == ':':
            newText += c
            newText += "\n\n"
            in_whitespace = True
        elif c == ' ':
            if not in_whitespace:
                newText += c
            in_whitespace = True
        else:
            in_whitespace = False
            newText += c
    if newText:
        print(newText, end="")
    else:
        newText = ""
        print(newText, end="")
