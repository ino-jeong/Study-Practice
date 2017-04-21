# bottom-up calculation


def get_playlist(p_length, p, x, y, m, value_hash):
    # let x is number of songs already listed
    # y is number of songs listed not yet
    # thus, x+y = n
    # p is current length of play list
    # value_hash is for memoization
    # this function uses top-down calculation

    # if p is n, this is last calculation.
    # in this case, number of songs not listed must be n, total number of songs
    if p_length == p:
        if y == 0:
            return 1
        else:
            return 0

    # memoization
    if (p_length, x, y) in value_hash:
        return value_hash[(p_length, x, y)]

    ans = 0
    # case1 : p'th song is new song, which is not listed yet before.
    if y > 0:
        ans += get_playlist(p_length + 1, p, x + 1, y - 1, m, value_hash) * y

    # case2 : p'th song is already listed before.
    # in this case, possible number of song is x - m,
    # because same song must be separated by m-songs
    if x - m > 0:
        ans += get_playlist(p_length + 1, p, x, y, m, value_hash) * (x - m)

    value_hash[(p, x, y)] = ans % 1000000007

    return value_hash[(p, x, y)]


nmp = input().split()
n = int(nmp[0])
m = int(nmp[1])
p = int(nmp[2])
value_hash = {}

# get play list of length p, all n songs are listed and no rest one.
print(get_playlist(0, p, 0, n, m, value_hash))
