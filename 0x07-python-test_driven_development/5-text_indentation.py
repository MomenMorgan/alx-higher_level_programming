#!/usr/bin/python3
"""
prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: . ? :

    Args:
        text : a string
    """
    newform = ""
    strr = ""
    temp = [] * 2
    flag = 0

    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if i < len(text) and text[i] == '.' or text[i] == '?'\
           or text[i] == ':':
            if flag == 0:
                temp = text.split(text[i], 1)
                flag = 1
            else:
                temp = strr.split(text[i], 1)
            newform += temp[0].lstrip(' ') + text[i]
            strr = temp[1]
            print("{:s}".format(newform))
            print()
            newform = ""
    if flag == 0:
        text = text.lstrip(' ')
        text = text.rstrip(' ')
        print("{:s}".format(text), end="")
    else:
        strr = strr.lstrip(' ')
        strr = strr.rstrip(' ')
        print("{:s}".format(strr), end="")
