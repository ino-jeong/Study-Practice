import queue

def hide_and_seek_4(n, k):
    if n == k:
        print(0)
        print(n)
        return

    data_queue = queue.Queue()
    visit_hash = {}

    cur = n
    cur_time = 0
    data_queue.put((cur, cur_time))
    visit_hash[cur] = True

    while cur != k:
        cur, cur_time = data_queue.get()

        if 2 * cur <= 100000 and (not (2 * cur) in visit_hash):
            data_queue.put((2 * cur, cur_time + 1))
            visit_hash[2 * cur] = cur

        if cur + 1 <= 100000 and (not (cur + 1) in visit_hash):
            data_queue.put((cur + 1, cur_time + 1))
            visit_hash[cur + 1] = cur

        if cur - 1 >= 0 and (not (cur - 1) in visit_hash):
            data_queue.put((cur - 1, cur_time + 1))
            visit_hash[cur - 1] = cur

    print(cur_time)

    # 1. stack 이용해 출력 할 경우
    visit_stack = queue.LifoQueue()
    route_check = k
    visit_stack.put(route_check)
    while route_check != n:
        route_check = visit_hash[route_check]
        visit_stack.put(route_check)

    while visit_stack.empty() is not True:
        print(visit_stack.get(),end=' ')

    # 2. 재귀함수 정의하여 출력 할 경우
#     print('\n')
#     print(route_print(visit_hash,n,k))
#
# def route_print(visit_hash, n, k):
#     if n == k:
#         return str(n)
#     return route_print(visit_hash, n, visit_hash[k])+ ' ' + str(k)


line_input = input()
line_input = line_input.split(' ')
n = int(line_input[0])
k = int(line_input[1])

hide_and_seek_4(n, k)