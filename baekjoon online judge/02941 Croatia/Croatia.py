input_str = input()

length = len(input_str)
length_correction = 0

for i in range(length):
    ch = input_str[i]

    if ch == '=':
        if (input_str[i-1] == 'c' or input_str[i-1] == 'z' or input_str[i-1] == 's') and i >= 1:
            length_correction += 1
            if input_str[i-1] == 'z' and input_str[i-2] == 'd' and i >= 2:
                length_correction += 1
    elif ch == '-':
        if (input_str[i-1] == 'c' or input_str[i-1] == 'd') and i >= 1:
            length_correction += 1
    elif ch == 'j':
        if (input_str[i-1] == 'l' or input_str[i-1] == 'n') and i >= 1:
            length_correction += 1

print(length - length_correction)
