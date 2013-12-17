def is_unique(string):
    for indexA, itemA in enumerate(string):
        for indexB, itemB in enumerate(string):
            if indexA != indexB:
                if itemA == itemB:
                    return False
    return True

print is_unique("abcderf")
