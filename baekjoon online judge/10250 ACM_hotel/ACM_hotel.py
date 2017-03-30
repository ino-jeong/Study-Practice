cases = int(input())

for c in range(cases):
    line_input = input()
    line_input = line_input.split(' ')

    h = int(line_input[0])
    w = int(line_input[1])
    n = int(line_input[2])

    x = (int(n)-1) // int(h) + 1

    if x < 10:
        x = '0' + str(x)
    else:
        x = str(x)

    y = int(n) % int(h)
    if y == 0:
        y = int(h)
    y = str(y)

    print(y+x)
