def check_group_word(input_str):

    chk_arr = [0] * 26
    offset = ord('a')
    cur = ''

    for i in range(len(input_str)):
        ch = input_str[i]
        if ch != cur:
            ch_idx = ord(ch) - offset
            if chk_arr[ch_idx] != 0:
                return False
            else:
                chk_arr[ch_idx] = 1
                cur = ch
        else:
            continue

    return True


n = int(input())
input_arr = []

for i in range(n):
    input_arr.append(input())

count = 0
for in_str in input_arr:
    if check_group_word(in_str) is True:
        count += 1

print(count)
