# Design an algorithm and write code to remove the duplicate characters in
 # a string without using any additional buffer NOTE One or two additional variables 
 # are fine An extra copy of the array is not



def remove_dup(string):
    new_string = ""
    for char in string:
        if char not in new_string:
            new_string += char
    return new_string

print remove_dup("GOOOSIAOOO")








