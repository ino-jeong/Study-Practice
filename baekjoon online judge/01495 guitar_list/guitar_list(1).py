n, s, m = map(int, input().split())

line_input = input().split()

volume_list = [0] * (n + 1)
volume_list[0] = s
for i in range(1, n + 1):
    volume_list[i] = int(line_input[i - 1])

volume_table = [[0] * (m + 1) for i in range(n + 1)]

memo_hash = {}

def check_volume(cur_vol, now):
    if now == n:
        for i in range(m, -1, -1):
            if volume_table[n][i] == 1:
                return i

    memo_hash[(cur_vol, now)] = True

    idx1 = -1
    idx2 = -1
    if cur_vol + volume_list[now + 1] <= m and (cur_vol + volume_list[now + 1], now + 1) not in memo_hash:
        volume_table[now + 1][cur_vol + volume_list[now + 1]] = 1
        idx1 = check_volume(cur_vol + volume_list[now + 1], now + 1)

    if cur_vol - volume_list[now + 1] >= 0 and (cur_vol - volume_list[now + 1], now + 1) not in memo_hash:
        volume_table[now + 1][cur_vol - volume_list[now + 1]] = 1
        idx2 = check_volume(cur_vol - volume_list[now + 1], now + 1)

    if idx1 == -1 and idx2 == -1:
        return -1
    else:
        return max(idx1, idx2)

print(check_volume(s, 0))
