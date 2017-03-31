class orderInfo:
    '''
    이 부분은 수정하지 마세요.
    '''

    def __init__(self, t, d, v):
        self.time = t
        self.duration = d
        self.vip = v


def processOrder(orders):
    '''
    주문 정보가 주어질 때, 주문이 처리되는 순서를 출력합니다.
    '''

    n = len(orders)
    current_time = orders[0].time
    current_idx = 0

    result = []
    normal_q = []
    vip_q = []

    # current_time >= 인 모든 line order들 normal/vip q 나눠서 넣는다.
    # vip 있을 경우 그것 먼저, 아닐경우 normal q에서 하나 꺼내서 처리
    # current_time을 duration 만큼 업데이트

    while current_idx < n:
        while current_time >= orders[current_idx].time:
            if orders[current_idx].vip == 1:
                vip_q.append((current_idx + 1, orders[current_idx].duration))
                current_idx += 1
            else:
                normal_q.append((current_idx + 1, orders[current_idx].duration))
                current_idx += 1
            if current_idx >= n:
                break

        if len(vip_q) > 0:
            temp = vip_q.pop(0)
            result.append(temp[0])
            current_time += temp[1]
        elif len(normal_q) > 0:
            temp = normal_q.pop(0)
            result.append(temp[0])
            current_time += temp[1]

    while len(vip_q) > 0:
        temp = vip_q.pop(0)
        result.append(temp[0])
        current_time += temp[1]

    while len(normal_q) > 0:
        temp = normal_q.pop(0)
        result.append(temp[0])
        current_time += temp[1]

    return result


######################################
'''
input_ex 1
ans 1 2 3 4
4
1 3 0
4 3 0
7 3 0
10 3 0


input_ex 2
ans 1 2 3 4
4
1 3 0
3 3 0
5 3 0
7 3 0

input_ex 3
ans 1 2 4 3
4
1 3 0
3 3 0
5 3 0
7 3 1

input_ex 4
ans 1 4 7 8 9 2 3 5 6
9
1 4 0
3 1 0
4 1 0
5 4 1
6 5 0
7 4 0
9 4 1
13 4 1
17 4 1

'''

p = int(input())
orders = []

for i in range(p) :
    myList = [int(v) for v in input().split(' ')]
    orders.append(orderInfo(myList[0], myList[1], myList[2]))

print(*processOrder(orders))