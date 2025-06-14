class UnionFind:
    def __init__(self, n):
        # Initially, each node is parent to itself
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n

    def findBasic(self, p):
        if self.parent[p] == p:
            return p
        return self.findBasic(self.parent[p])

    def unionBasic(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        self.parent[rootP] = rootQ

    def findPathCompression(self, p):
        if self.parent[p] != p:
            # path compression
            self.parent[p] = self.findPathCompression(self.parent[p])
        return self.parent[p]

    def unionByRank(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return

        if self.rank[rootP] < self.rank[rootQ]:
            self.parent[rootP] = rootQ
        elif self.rank[rootP] > self.rank[rootQ]:
            self.parent[rootQ] = rootP
        else:
            # you can switch P and Q if you wish
            self.parent[rootP] = rootQ
            self.rank[rootQ] += 1

    def unionBySize(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return
        if self.size[rootP] < self.size[rootQ]:
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
        else:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
