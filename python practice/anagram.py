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
# print(str1.upper())

############## or ##############
#
# def anagram(str1, str2):
#     str1 = str1.lower()
#     str2 = str2.lower()
#
#     str1 = sorted(str1)
#     str2 = sorted(str2)
#
#     str1 = ''.join(str1)
#     str2 = ''.join(str2)
#
#     str1 = str1.strip()
#     str2 = str2.strip()
#
#     if str1 == str2:
#         return True
#     else:
#         return False
#
# print(anagram(str1, str2))
