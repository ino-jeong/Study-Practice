def is_unique (str):
    if len(str) > 256:
        return False

    hash_arr = [False] * 256

    for ch in str:
        if hash_arr[ord(ch)] is True:
            return False
        else:
            hash_arr[ord(ch)] = True
    return True

str = 'gaAzZtu yiop'
print(is_unique(str))

