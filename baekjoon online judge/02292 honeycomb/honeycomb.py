def last_room(route):
    result = 1 + 6 * (route - 1) * route / 2
    return int(result)

n = int(input())

route = 1
while last_room(route) < n:
    route += 1

print(route)
