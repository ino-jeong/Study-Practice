import stack_practice

def reverse(str):
    length = len(str)
    reversed = ''

    for i in range(length-1,-1,-1):
        ch = str[i]
        reversed = reversed + ch

    return reversed

str = 'abcdefg'
print(reverse(str))

#################### or ####################

def reverse_by_stack(str):
    ch_stack = stack_practice.Stack()

    for ch in str:
        ch_stack.push(ch)

    output = ''

    while not ch_stack.is_empty():
        output += ch_stack.pop()

    return output

print(reverse_by_stack(str))