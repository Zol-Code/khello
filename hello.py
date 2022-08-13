import sys

<<<<<<< HEAD
length = len(sys.argv)
if length == 2:
    name = sys.argv[1]

    if name == "--version":
        print("KHello version 1.0")
        print("All rights reverved. Zolla Software Company")
    else:
        print("Hello", name + "!")
=======
if name == "--version":
    print("KHello version 1.1")
    print("All rights reverved. Zolla Software Company")
>>>>>>> CHanged version number
else:
    print("Enter name")

