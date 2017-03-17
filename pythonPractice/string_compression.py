def str_comp(input_str):

    output_char = input_str[0]
    output = [output_char]
    count = 1

    for i in range(1,len(input_str)):
        ch = input_str[i]
        if output_char == ch:
            count += 1
        else:
            output.append(str(count))
            output_char = ch
            output.append(output_char)
            count = 1
    output.append(str(count))

    result = ''.join(output)
    if len(input_str) <= len(result):
        return input_str
    else:
        return result


input_str = 'aaabbcDDDDDtt'

print(str_comp(input_str))
