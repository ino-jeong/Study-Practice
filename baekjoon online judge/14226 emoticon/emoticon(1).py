class Queue():
    def __init__(self):
        self.current = []
        self.clipboard = []
        self.time = []

    def put(self, cur, clip, t):
        self.current.append(cur)
        self.clipboard.append(clip)
        self.time.append(t)

    def get(self):
        return (self.current.pop(0), self.clipboard.pop(0), self.time.pop(0))

    def is_empty(self):
        if len(self.current) > 0:
            return False
        else:
            return True


def min_time(s):

    emo_queue = Queue()
    visit = {}
    visit[s] = s
    cur = 1
    clip = 0
    time = 0

    emo_queue.put(cur, clip, time)
    visit[cur] = time

    while emo_queue.is_empty() is not True:
        cur, clip, time = emo_queue.get()

        if cur == s:
            

        # 1. clipboard에 내용 있을 때 붙여넣기, 1초 소요
        if clip > 0 and (cur + clip) not in visit:
            if (cur + clip) <= (s + clip):
                emo_queue.put(cur + clip, clip, time + 1)
                visit[cur + clip] = time + 1

        # 3. 현재 내용에서 1개 삭제하기
        if (cur - 1) >= 2 and (cur - 1) not in visit:
            emo_queue.put(cur - 1, clip, time + 1)
            visit[cur - 1] = time + 1

        # 2. 현재 내용을 clipboard 복사 후 붙여넣기, 2초 소요
        if (2 * cur) not in visit:
            if (2 * cur) <= 1024:
                emo_queue.put(2 * cur, cur, time + 2)
                visit[2* cur] = time + 2


    print(time)

s = int(input())
min_time(s)