def next_permutation(perm):

    # input permutation : string
    # working in function as array (converting it temporary

    input_arr = str_to_arr(perm)

    i = len(input_arr) - 1
    while i > 0 and input_arr[i-1] >= input_arr[i]:
        i -= 1

    if i <= 0:
        print('this is last permutation')
        return perm

    j = len(input_arr) - 1
    while input_arr[j] <= input_arr[i - 1]:
        j -= 1

    input_arr[i - 1], input_arr[j] = input_arr[j], input_arr[i - 1]

    j = len(input_arr) - 1
    while i < j:
        input_arr[i], input_arr[j] = input_arr[j], input_arr[i]
        i += 1
        j -= 1

    perm_output = arr_to_str(input_arr)
    return perm_output

def str_to_arr(str):
    arr = []

    for s in str:
        arr.append(s)

    return arr

def arr_to_str(arr):
    str_output = ''

    for a in arr:
        str_output = str_output + str(a)

    return str_output

# next_permutation test

test_perm = '1234'
print('permutation this time :', test_perm)
print('next permutation :', next_permutation(test_perm))
