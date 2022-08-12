import sys
name = sys.argv[1]

if name == "--version":
    print("KHello version 1.0")
    print("All rights reverved. Zolla Software Company")
else:
    print("Hello", name + "!")

