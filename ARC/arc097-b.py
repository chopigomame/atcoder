import collections
import itertools
import operator
from typing import List, Dict

def getInputs():
    N, M = map(int, input().split())
    ps = list(map(int, input().split()))
    xys = []
    for _ in range(M):
        xys.append(list(map(int, input().split())))
    return N, M, ps, xys

class UnionFind:
    def __init__(self, elems=None):
        class KeyDict(dict):
            def __missing__(self, key):
                self[key] = key
                return key

        self.parent = KeyDict()
        self.rank = collections.defaultdict(int)

        if elems is not None:
            for elem in elems:
                _, _ = self.parent[elem], self.rank[elem]

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

    def are_same(self, x, y):
        return self.find(x) == self.find(y)
    
    def grouper(self):
        roots = [(x, self.find(x_par)) for x, x_par in self.parent.items()]
        root = operator.itemgetter(1)
        for _, group in itertools.groupby(sorted(roots, key=root), root):
            yield [x for x, _ in group]

    def get_group(self, x):
        root = self.find(x)
        group = [y for y, par in self.parent.items() if self.find(par) == root]
        return group

def solve(ps, xys):
    uf = UnionFind()
    for xy in xys:
        uf.unite(xy[0], xy[1])
    validCount = 0
    for i, p in enumerate(ps):
        if p != i+1:
            if uf.are_same(i+1, p):
                validCount += 1
        else:
            validCount += 1
    print(validCount)

N, M, ps, xys = getInputs()
solve(ps, xys)