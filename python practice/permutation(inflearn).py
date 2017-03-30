# permutation implementation practice

input_arr = ['a', 'b', 'c']


def perm(input, i):
    if i == len(input)-1:
        print(input)
    else:
        for j in range(i, len(input)):
            input[i], input[j] = input[j], input[i]
            perm(input, i + 1)
            input[i], input[j] = input[j], input[i]

perm(input_arr, 0)