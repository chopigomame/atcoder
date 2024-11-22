from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

def get_inputs():
    H, W = map(int, input().split())
    Q = int(input())
    return H, W, Q

def solve():
    H, W, Q = get_inputs()
    box = [[0 for _ in range(W)] for _ in range(H)]
    ds = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    uf = UnionFind(H*W)

    for _ in range(Q):
        query = list(map(int, input().split()))
        q = query[0]
        if q == 1:
            r, c = query[1:]
            r, c = r-1, c-1
            box[r][c] = 1
            me = r * W + c
            for dy, dx in ds:
                tonari = (r + dy) * W + (c + dx)
                if not 0 <= r + dy < H or not 0 <= c + dx < W:
                    continue
                if box[r+dy][c+dx] == 1:
                    uf.union(me, tonari)
                    
        else:
            ra, ca, rb, cb = query[1:]
            ra, ca, rb, cb = ra-1, ca-1, rb-1, cb-1
            a = ra * W + ca
            b = rb * W + cb
            if box[ra][ca] != 1 or box[rb][cb] != 1:
                print("No")
            elif uf.same(a, b):
                print("Yes")
            else:
                print("No")

solve()