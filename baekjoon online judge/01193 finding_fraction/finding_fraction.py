def group_end(i):
    return i * (i + 1) / 2


def which_group(x):
    if x == 1:
        return 1

    i = 2
    while True:
        pre_group = group_end(i - 1)
        cur_group = group_end(i)
        if pre_group < x <= cur_group:
            break
        i += 1
    return i

x = int(input())

if x == 1:
    print('1/1')
else:
    group = which_group(x)
    group_sum = group + 1
    group_idx = x - group_end(group - 1)  # starting from 1

    numerator = str(int(group_idx))
    denominator = str(int(group_sum - group_idx))

    if group % 2 == 0:
        print(numerator+'/'+denominator)
    else:
        print(denominator+'/'+numerator)
