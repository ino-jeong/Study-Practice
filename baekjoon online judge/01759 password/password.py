def is_valid(pw):
    ja = 0
    mo = 0

    for ch in pw:
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            mo += 1
        else:
            ja += 1

    return (ja >= 2 and mo >= 1)


def check_pw(length, ch_set, pw, ch_idx):

    if len(pw) == length and is_valid(pw):
        print(pw)
        return

    if ch_idx >= len(ch_set):
        return

    check_pw(length, ch_set, pw + ch_set[ch_idx], ch_idx + 1)
    check_pw(length, ch_set, pw, ch_idx + 1)

lc = input().split()
length = int(lc[0])
c = int(lc[1])

ch_set = input().split()
ch_set.sort()

check_pw(length, ch_set, "", 0)
