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
        print('-1')
        return

    j = len(perm) - 1
    while perm[j] <= perm[i - 1]:
        j -= 1

    perm[i - 1], perm[j] = perm[j], perm[i - 1]

    j = len(perm) - 1
    while i < j:
        perm[i], perm[j] = perm[j], perm[i]
        i += 1
        j -= 1

    for p in perm:
        print(p, end=' ')

    return


n = int(input())
perm = input()

next_permutation(perm)

