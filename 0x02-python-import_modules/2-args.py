#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_args = len(sys.argv) - 1

    if num_args == 0:
        print("{:d} arguments.".format(num_args))
    elif num_args == 1:
        print("{:d} argument:".format(num_args))
    else:
        print("{:d} arguments:".format(num_args))

    if num_args >= 1:
        num_args = 0
        for arg in sys.argv:
            if num_args != 0:
                print("{:d}: {:s}".format(num_args, arg))
            num_args += 1
