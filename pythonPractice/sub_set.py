test_set = ['a', 'b', 'c']

# if n is n'th element of test set, then :
#
# n = 0,
# f(n=0) = []
#
# n = 1
# f(1) = f(0) + f(0)&set(1)
#
# n = 2
# f(2) = f(1) + f(1)&set(2)
#
# ...


def sub_set(input_set, n):
    # if n is zero(0), no element is selected thus return empty set, written as 'Φ' in this function
    if n == 0:
        return ['Φ']

    # first, get subset of (n-1) == before_set
    # copy before_set, and then attach n'th element (==element_now) at each item in before_set.
    # after attaching work done, merge that (== after_set) into before_set and return
    element_now = input_set[n - 1]  # eleement which to be attached
    before_set = sub_set(input_set, n-1)  # sub set from n-1
    after_set = []  # sub set which will be merged into before_set

    for element in before_set:
        # if element will be attached is empty set, ignore it and just attach new element
        if element == 'Φ':
            after_set.append(element_now)
            continue
        after_set.append(element + ', ' + element_now)

    return before_set + after_set


set_length = len(test_set)
result = sub_set(test_set, set_length)

print('all sub set of', test_set, 'is :')
print(result)
print('number of sub set is :', len(result))
