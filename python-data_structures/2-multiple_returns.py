# !/usr/bin/python3

def multiple_returns(sentence):

    length = len(sentence)
    first = sentence[0]
    newTuple = (length, first)

    if sentence == "":
        length = 0
        first = None
        return newTuple

    return newTuple


if __name__ == "__main__":
    multiple_returns()