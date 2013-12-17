# Perform string compression. If compressed string is the same as original: return original


def string_compression(string):
    d = {}
    for item in string:
        if d.get(item) != None:
            d[item] = d[item] + 1
        else:
            d[item] = 1
    result = []
    for key, val in d.iteritems():
        result.append(key)
        result.append(val)
    str_len = len(string)
    result = ''.join(result)
    compressed_len = len(result)
    if str_len != compressed_len:
        return compressed_len
    else:
        return str_len


print string_compression("aaddvvdffe")