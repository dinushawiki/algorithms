class Quick_find_uf:

    def __init__(self):
        self.ids = []

    def quickFindUf(self, n):
        self.ids = [0] * n
        for i in range(n):
            self.ids[i] = i
        print(self.ids)

    def isConnected(self, p, q):
        if self.ids[p] == self.ids[q]:
            return True
        else:
            return False

    def join(self, p, q):
        pid = self.ids[p]
        qid = self.ids[q]
        for i in range(len(self.ids)):
            if self.ids[i] == pid:
                self.ids[i] = qid


test = Quick_find_uf()
test.quickFindUf(6)
print(test.isConnected(0, 5))
test.join(0, 5)
print(test.isConnected(0, 5))
