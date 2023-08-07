# !/usr/bin/python3

def multiple_returns(sentence):
    newTuple = ()
    if sentence == "":
        return newTuple(None)
    
    length = len(sentence)
    first = sentence[0]
    newTuple = (length, first)

    return newTuple


if __name__ == "__main__":
    multiple_returns()