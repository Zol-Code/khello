import sys

length = len(sys.argv)
if length == 2:
    name = sys.argv[1]

    if name == "--version":
        print("KHello version 1.1")
        print("All rights reverved. Zolla Software Company")
    else:
        print("Hello", name + "!")
else:
    print("Enter name")

