#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_num =  len(sys.argv) - 1
    print("{}".format(arg_num), end="")
    if arg_num == 1:
        print("argument:")
    else:
        if arg_num != 0:
            print(":")
        else:
            print(".")
    
    for a in range(1, arg_num):
        print("{}: {}".format(a, sys.argv[a]))