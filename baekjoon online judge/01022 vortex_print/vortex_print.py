
def fst(n):  # return n-groups first element
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return 4 * n * (n-1) + 2


def cord_to_num(row, col):
    x = col
    y = row

    group_num = max(abs(x), abs(y))
    group_first = fst(group_num)
    group_delta = 0

    if group_num == 0:
        check_tuple = [0, 0]
    else:
        check_tuple = [group_num, group_num -1]

    delta_tuple = [0, -1]

    while check_tuple != [x, y]:
        # print('** check tuple :', check_tuple)
        # print('** [x, y] :', [x, y])
        check_tuple[0] += delta_tuple[0]
        check_tuple[1] += delta_tuple[1]
        group_delta += 1

        if check_tuple[0] > group_num and check_tuple[1] > group_num:
            print('something wrong input... return -1')
            return -1

        if check_tuple[0] == group_num and check_tuple[1] == group_num * -1:
            delta_tuple[0] = -1
            delta_tuple[1] = 0
        elif check_tuple[0] == group_num * -1 and check_tuple[1] == group_num * -1:
            delta_tuple[0] = 0
            delta_tuple[1] = 1
        elif check_tuple[0] == group_num * -1 and check_tuple[1] == group_num:
            delta_tuple[0] = 1
            delta_tuple[1] = 0

    return group_first + group_delta


def num_length(num):
    num = str(num)
    return len(num)

line_input = input()
line_input = line_input.split(' ')

r1 = int(line_input[0])
c1 = int(line_input[1])
r2 = int(line_input[2])
c2 = int(line_input[3])

# array index = real index + offset
# real index = array index - offset
row_offset = r1
col_offset = c1
width = (c2 - c1 + 1)
height = (r2 - r1 + 1)

data_array = []
max_element = 0

for row in range(height):
    row_data = []
    for col in range(width):
        real_idx = [row + row_offset, col + col_offset]
        element = cord_to_num(real_idx[0], real_idx[1])
        if element > max_element:
            max_element = element
        row_data.append(element)
    data_array.append(row_data)

max_length = num_length(max_element)

for row in data_array:
    for row_idx in range(len(row)):
        ele_length = num_length(row[row_idx])
        padding_cnt = max_length - ele_length

        row[row_idx] = str(row[row_idx])
        for i in range(padding_cnt):
            row[row_idx] = ' ' + row[row_idx]

        if row_idx == len(row) - 1:
            print(row[row_idx],end='')
        else:
            print(row[row_idx],end=' ')
    print('')
