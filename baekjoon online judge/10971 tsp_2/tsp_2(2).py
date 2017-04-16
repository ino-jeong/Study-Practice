def next_permutation(perm):

    i = len(perm) - 1
    while i > 0 and perm[i-1] >= perm[i]:
        i -= 1

    if i <= 0:
        return False

    j = len(perm) - 1
    while perm[j] <= perm[i - 1]:
        j -= 1

    perm[i - 1], perm[j] = perm[j], perm[i - 1]

    j = len(perm) - 1
    while i < j:
        perm[i], perm[j] = perm[j], perm[i]
        i += 1
        j -= 1

    return True


# get input data
n = int(input())
W = []

for i in range(n):
    line_input = input().split(' ')
    temp = []
    for j in range(n):
        temp.append(int(line_input[j]))

    W.append(temp)


# first permutation
d = []
for i in range(1,n):
    d.append(i)

ans = 2**31 - 1


ok = True
sum = 0
for i in range (n-2):
    if W[d[i]][d[i+1]] == 0:
        ok = False
    else:
        sum += W[d[i]][d[i+1]]

if ok and W[0][d[0]]!=0 and W[d[n-2]][0]!=0:
    sum += W[0][d[0]] + W[d[n-2]][0]
    ans = min(sum, ans)

while(next_permutation(d)):
    ok = True
    sum = 0
    for i in range(n - 2):
        if W[d[i]][d[i + 1]] == 0:
            ok = False
        else:
            sum += W[d[i]][d[i + 1]]

    if ok and W[0][d[0]]!=0 and W[d[n-2]][0]!=0:
        sum += W[0][d[0]] + W[d[n-2]][0]
        ans = min(sum, ans)

print(ans)
