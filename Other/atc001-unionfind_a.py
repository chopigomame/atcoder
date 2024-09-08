import collections
import itertools
import operator
from typing import List, Dict

def getInputs():
    N, Q = map(int, input().split())
    inputs = []
    for _ in range(Q):
        type, a, b = map(int, input().split())
        inputs.append([type, a, b])
    return N, inputs

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

def solve(commands):
    uf = UnionFind()
    for command in commands:
        type, a, b = command
        if type == 0:
            uf.unite(a, b)
        if type == 1:
            if uf.are_same(a, b):
                print("Yes")
            else:
                print("No")

N, commands = getInputs()
solve(commands)