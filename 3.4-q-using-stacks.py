class Qstack:
    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self, d):
        self.instack.append(d)

    def dqueue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()


if __name__ == '__main__':
    q = Qstack()
    for i in range(10):
        q.enqueue(i)
    print(q.instack)
    for i in xrange(10):
        print(q.dqueue()),


