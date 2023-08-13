#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        charac = None
        length = 0
        myTuple = (length, charac)
        return myTuple
    else:
        charac = sentence[0]
        length = len(sentence)
        myTuple = (length, charac)
        return myTuple
