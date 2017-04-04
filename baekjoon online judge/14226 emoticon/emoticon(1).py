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
        return self.current.pop(0), self.clipboard.pop(0), self.time.pop(0)

    def is_empty(self):
        if len(self.current) > 0:
            return False
        else:
            return True


def min_time(s):

    emo_queue = Queue()
    visit = {}
    cur = 1
    clip = 0
    time = 0

    emo_queue.put(cur, clip, time)
    visit[(cur,clip)] = True

    while cur != s:
        cur, clip, time = emo_queue.get()

        # 1. clipboard에 내용 있을 때 붙여넣기, 1초 소요
        if clip > 0 and (cur + clip, clip) not in visit:
            emo_queue.put(cur + clip, clip, time + 1)
            visit[(cur + clip), clip] = True

        # 2. 현재 내용을 clipboard 복사 하기, 1초 소요
        if (cur, cur) not in visit:
            emo_queue.put(cur, cur, time + 1)
            visit[(cur, cur)] = True

        # 3. 현재 내용에서 1개 삭제하기
        if (cur - 1) >= 2 and (cur - 1, clip) not in visit:
            emo_queue.put(cur - 1, clip, time + 1)
            visit[(cur - 1, clip)] = True

    print(time)


s = int(input())
min_time(s)