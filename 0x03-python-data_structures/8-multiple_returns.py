#!/usr/bin/python3
def multiple_returns(sentence):
    new_s = (len(sentence), )
    if len == 0:
        return (new_s + (None,))
    else:
        return(new_s + (sentence[0],))
