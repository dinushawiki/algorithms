class Quick_union_uf:

    def __init__(self):
        self.ids = []

    def quickFindUf(self, n):
        self.ids = [0] * n
        for i in range(n):
            self.ids[i] = i
        print(self.ids)

    def findRoot(self, i):
        while (i != self.ids[i]):
            i = self.ids[i]
        return i

    def isConnected(self,p,q):
        return self.findRoot(p) == self.findRoot(q)

    def join(self, p, q):
        root_p = self.findRoot(p)
        root_q = self.findRoot(q)
        self.ids[root_p] = root_q

test = Quick_union_uf()
test.quickFindUf(5)
print(test.findRoot(0))
print(test.isConnected(0,1))
test.join(0,1)
print(test.isConnected(0,1))
test.join(3,4)
test.join(0,4)
print(test.isConnected(1,4))