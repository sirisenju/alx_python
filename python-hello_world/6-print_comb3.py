# !/usr/bin/python3
combination = True
for i in range(0, 10):
    for j in range(i+1, 10):
        if not combination:
            print(", ", end="")
        combination = False
        print("{}{}".format(i, j), end="")
print()