# Write code to reverse a C-Style String C-String means that 'abcd' is represented 
# as five characters including the null character )


def reverse_C_style(string):
    reverse = []
    string = string[:-2]
    for index in range(len(string)):
        reverse.append(string[len(string) - index - 1])
    reverse.append('/0')
    return ''.join(reverse)

print reverse_C_style("Gosia/0")
