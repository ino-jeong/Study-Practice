def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    hash_arr1 = [0] * 256
    hash_arr2 = [0] * 256

    for ch in str1:
        # if you want to consider upper and lower case same, uncomment this if statement
        # if 122 >= ord(ch) >= 97:
        #     ch = chr(ord(ch) - 32)
        hash_arr1[ord(ch)] += 1

    for ch in str2:
        # if 122 >= ord(ch) >= 97:
        #     ch = chr(ord(ch) - 32)
        hash_arr2[ord(ch)] += 1

    for i in range(256):
        if hash_arr1[i] != hash_arr2[i]:
            return False

    return True

str1 = ' abc defg'
str2 = 'b c defga'

print(is_anagram(str1, str2))
