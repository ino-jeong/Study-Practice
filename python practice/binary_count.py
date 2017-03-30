# convert certain number(dec) into binary number,
# and then count number of one(1) in the converted one


def binary_count(n):
    rest = n
    binary = []
    count = 0

    i = 0
    while rest >= 2 ** i:
        i += 1

    for exp in range(i - 1, -1, -1):
        if rest >= 2 ** exp:
            rest -= 2 ** exp
            binary.append(1)
            count += 1
        else:
            binary.append(0)

    result = count
    return result

print(binary_count(8))
