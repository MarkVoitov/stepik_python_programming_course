update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    else:
        if key * 2 in d:
            d[key * 2].append(value)
        else:
            d[key * 2] = [value]
    return d