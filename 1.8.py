# Assume you have a method isSubstring which checks if one word is 
# a substring of another Given two strings, s1 and s2, write code to check 
# if s2 is a rotation of s1 using only one call to isSubstring (waterbottle is
# a rotation of erbottlewat)

def is_longer1(str1, str2):
    if len(str1) > len(str2):
        return str1
    else:
        return str2

def is_shorter1(str1, str2):
    if len(str1) > len(str2):
        return str2
    else:
        return str1


def is_sub_as_shorter(shorter, substring):
    for i in range(len(shorter)):
        for j in range(len(substring)):
            if i == j:
                if shorter[i] != substring[j]:
                    return False
    return True


def is_substring1(str1, str2):
    longer = is_longer1(str1, str2)
    shorter = is_shorter1(str1, str2)
    for i in range(len(shorter)):
        for j in range(len(longer)):
            if shorter[i] == longer[j]:
                substring = longer[j:len(shorter) + j]
                print substring, shorter
                if is_sub_as_shorter(shorter, substring) == True:
                    return True
    return False


print is_substring1("rfrnhbgaka","aka")
print is_substring1("rfrfrakajunhbg","sss")
print is_substring1("sskk","sss")




def is_substring2(longer, shorter):
    for j in range(len(longer) - len(shorter)):
        if shorter[0] == longer[j]:
            substring = longer[j:len(shorter) + j]
            print substring, shorter
            if shorter == substring:
                return True
    return False

            

def is_rotation(s1, s2):
    s2 = s2 + s2
    if is_substring2(s2, s1) == True:
        print "Is rotation"
    else:
        print "It is not rotation"

is_rotation("waterbottle", "erbottlewat")























