def space_to_20(str):
    output_arr = []

    for start in range(len(str)):
        if str[start] != ' ':
            break

    for end in range(len(str)-1, -1, -1):
        if str[end] != ' ':
            break

    for i in range(start,end+1):
        ch = str[i]
        if ch == ' ':
            ch = '%20'
        output_arr.append(ch)

    result = ''.join(output_arr)

    return result

str = ' AT YZZ  ' # to 'AT%20YZZ', outer space is removed
print(space_to_20(str))