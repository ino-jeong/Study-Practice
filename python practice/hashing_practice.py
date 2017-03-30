

class Hashing():
    def __init__(self, size):
        self.data = [(None, None)] * size

    def put(self, k, x):
        idx = self.transfrom_func(k)

        for i in range(len(self.data)):
            if self.data[idx][0] is None:
                self.data[idx] = k,x
                return
            else:
                idx = (idx + 1) % len(self.data)

        print("no space anymore... can't save data")

    def get(self,k):
        idx = self.transfrom_func(k)

        for i in range(len(self.data)):
            if self.data[idx][0] == k:
                return self.data[idx][1]
            else:
                idx = (idx + 1) % len(self.data)

        print("no data with key value %d" % k)
        return None

    def transfrom_func(self, k):
        return k % len(self.data)

    def status(self):
        print(self.data)



hashing = Hashing(10)
hashing.status()

hashing.put(3,9)
hashing.put(40,10)
hashing.put(105,11)
hashing.put(1236,12)
hashing.put(57,13)
hashing.put(851,14)
hashing.put(911,15)
hashing.put(120,16)
hashing.put(1151,17)
hashing.put(1542,18)

hashing.put(13,20)

hashing.status()

print(hashing.get(1151))