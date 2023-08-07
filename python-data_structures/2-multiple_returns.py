# !/usr/bin/python3

def multiple_returns(sentence):
    if sentence == " " or sentence == "":
        return None
    
    length = len(sentence)
    first = sentence[0]
    newTuple = (length, first)

    return "Length: {:d} - First character: {}".format(newTuple[0], newTuple[1])


if __name__ == "__main__":
    multiple_returns()