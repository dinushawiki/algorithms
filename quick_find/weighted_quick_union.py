class Weighted_quick_union_uf:
    def __int__(self):
        self.ids = []
        self.size = []

    def quickFindUf(self, n):
        self.ids = [0] * n
        self.size = [0] * n
        for i in range(n):
            self.ids[i] = i
            self.size[i] = 1
        print(self.ids)
        print(self.size)

    def findRoot(self, i):
        while (i != self.ids[i]):
            i = self.ids[i]
        return i

    def isConnected(self, p, q):
        return self.findRoot(p) == self.findRoot(q)

    def join(self, p, q):
        root_p = self.findRoot(p)
        root_q = self.findRoot(q)
        if root_p == root_q:
            return
        if (self.size[p] < self.size[q]):
            self.ids[root_p] = root_q
            self.size[root_q] += self.size[root_p]
        else:
            self.ids[root_q] = root_p
            self.size[root_p] += self.size[root_q]
        print(self.ids, self.size)

    def find(self, i):
        root = self.findRoot(i)
        print(self.ids.index(root))
        print(self.largest(root))

    def largest(self, i):
        if i not in self.ids:
            return i
        return self.largest(self.ids.index(i))

test = Weighted_quick_union_uf()
test.quickFindUf(5)
print(test.findRoot(0))
print(test.isConnected(0, 1))
test.join(0, 1)
print(test.isConnected(0, 1))
test.join(0, 2)
print(test.isConnected(1, 2))
test.find(0)
