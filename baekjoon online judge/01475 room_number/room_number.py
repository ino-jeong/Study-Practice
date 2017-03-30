import math

n = int(input())

num_set = [0]*10

while n != 0:
    target = n % 10
    num_set[target] += 1
    n //= 10

num_share = math.ceil((num_set[6] + num_set[9]) / 2)
num_set[6] = num_share
num_set[9] = num_share

print(max(num_set))
