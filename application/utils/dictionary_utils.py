def increment(dictionary, key):
    if dictionary.get(key) is None:
        dictionary[key] = 0

    dictionary[key] += 1
