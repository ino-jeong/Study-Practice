class Queue():
    def __init__(self):
        self.position = []
        self.time = []

    def put(self, pos, t):
        self.position.append(pos)
        self.time.append(t)

    def get(self):
        return (self.position.pop(0), self.time.pop(0))

    def is_empty(self):
        if len(self.position) > 0:
            return False
        else:
            return True



