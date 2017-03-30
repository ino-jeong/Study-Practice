cases = int(input())

for c in range(cases):
    line_input = input()
    stack = []
    vps ='YES'

    for ch in line_input:
        if ch == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                vps = 'NO'
            else:
                stack.pop()

    if len(stack) != 0:
        vps = 'NO'

    print(vps)
