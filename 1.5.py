# Write a method to replace all spaces in a string with '%20'

def replace_string(string):
    lista = string.split(" ")
    result = []
    for item in lista:
        result.append(item)
        result.append('%20')
    return ''.join(result)

print replace_string("hahaha ndndn")

