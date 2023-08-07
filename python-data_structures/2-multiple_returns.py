# !/usr/bin/python3

def multiple_returns(sentence):

    if sentence == "":
        length = 0
        first = None
        newTuple = (length, first)
        return newTuple

    length = len(sentence)
    first = sentence[0]
    newTuple = (length, first)
    return newTuple


if __name__ == "__main__":
    multiple_returns()