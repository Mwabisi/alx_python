#!/usr/bin/python3
 import sys
def main(argv):
     if len(argv) == 1:
         print("0 arguments.")
     elif len(argv) == 2:
         print("1 argument:")
     else:
         print("{} arguments:".format(len(argv) - 1))
     for i in range(1, len(argv)):
         print("{}: {}".format(i, argv[i]))
 if __name__ == "__main__":
     main(sys.argv)