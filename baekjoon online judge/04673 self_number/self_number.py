# function d(n) : sum n and its each order's number
# for example, d(75) = 75 + 7 + 5 = 87
def d(n):
    result = n

    while n != 0:
        result += (n % 10)
        n = n // 10

    return result

# has_n() function will check out if certain number 'num' has 'n' such that d(n) = num
def has_n(num):
    exp = 0
    copy = num

    while copy != 0:
        exp += 1
        copy = copy // 10

    # if 'num' has 'n', 'n' shall be located in range of (num itself - 1, certain minimum)
    # and that minimum shall be 'num - 9 * order of num'. due to maximum number of each order is '9'
    min_range = num - 9 * exp

    for n in range(num - 1, min_range - 1 , -1):
        # if n goes negative, there is no n
        if n < 0:
            return False

        if d(n) == num:
            return True

    return False

# if certain number 'num' has no number 'n' such that d(n) = num, than 'num' is 'self number'
# check out and print self numbers within range of [1,10000]
for test_num in range(1,10001):
    if has_n(test_num) is False:
        print(test_num)