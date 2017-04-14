def next_permutation(perm):

    # input permutation : string
    # working in function as array (converting it temporary

    perm = perm.split(' ')

    for p_idx in range(len(perm)):
        perm[p_idx] = int(perm[p_idx])

    i = len(perm) - 1
    while i > 0 and perm[i-1] >= perm[i]:
        i -= 1

    if i <= 0:
        return -1

    j = len(perm) - 1
    while perm[j] <= perm[i - 1]:
        j -= 1

    perm[i - 1], perm[j] = perm[j], perm[i - 1]

    j = len(perm) - 1
    while i < j:
        perm[i], perm[j] = perm[j], perm[i]
        i += 1
        j -= 1

    str_output = str(perm[0])
    for p in perm[1:]:
        str_output = str_output + ' ' + str(p)

    return str_output

n = int(input())
cur_permutation = '1'

for i in range(2, n+1):
    cur_permutation = cur_permutation + ' ' + str(i)


while cur_permutation != -1:
    print(cur_permutation)
    cur_permutation = next_permutation(cur_permutation)

