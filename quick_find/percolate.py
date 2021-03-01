class Percolate:
    def __int__(self):
        self.ids = [[]]
        self.size = [[]]

    def percolateuf(self, n):
        self.ids = [0] * n
        self.size = [0] * n
        for i in range(n):
            self.ids[i] = i
            self.size[i] = 1
        print(self.ids)

    def findRoot(self, i):
        while i != self.ids[i]:
            i = self.ids[i]
        return i

    def isConnected(self, p, q):
        return self.ids[p] == self.ids[q]

    def join(self, p, q):
        root_p = self.findRoot(p)
        root_q = self.findRoot(q)
        if root_p == root_q:
            return
        if self.size[p] < self.size[q]:
            self.ids[root_p] = root_q
            self.size[root_q] += self.size[root_p]
        else:
            self.ids[root_q] = root_p
            self.size[root_p] += self.size[root_q]
        print(self.ids, self.size)


test = Percolate()
test.percolateuf(18)
print(test.isConnected(0, 17))
test.join(0, 1)
test.join(0, 2)
test.join(0, 3)
test.join(0, 4)
test.join(2, 7)
test.join(7, 8)
test.join(7, 11)
test.join(8, 11)
test.join(11, 16)
test.join(13, 17)
test.join(14, 17)
test.join(15, 17)
test.join(16, 17)
print(test.isConnected(0, 16))
