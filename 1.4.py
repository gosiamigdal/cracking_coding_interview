# Write a method to decide if two strings are anagrams or not

def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    str1 = str1.lower()
    str2 = str2.lower()
    list1 = []
    list2 = []
    for item in str1:
        list1.append(item)
    for item in str2:
        list2.append(item)
    list1 = sorted(list1)
    list2 = sorted(list2)
    return list1 == list2


print is_anagram("aka","aap")