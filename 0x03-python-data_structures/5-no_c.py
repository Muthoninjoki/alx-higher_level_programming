#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for l in range(len(my_string)):
        if my_string[l] == "c" or my_string[l] == "C":
            pass
        else:
            new_string += my_string[l]
    return new_string
