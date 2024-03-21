#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    h = len(argv) - 1
    if h == 0:
        print("0 arguments.")
    elif h == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(h))
    for i in range(h):
        print("{}: {}".format(i + 1, argv[i + 1]))
