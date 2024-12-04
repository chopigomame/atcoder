import collections
import itertools
import operator
from typing import List, Dict

def getInputs():
    N, K, L = map(int, input().split())
    roads = []
    for _ in range(K):
        p, q = map(int, input().split())
        roads.append([p, q])
    rails = []
    for _ in range(L):
        p, q = map(int, input().split())
        rails.append([p, q])
    return N, roads, rails

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

def solve(N, commandsRoads, commandsRail):
    ufRoad = UnionFind()
    ufRail = UnionFind()
    for commandRoad in commandsRoads:
        a, b = commandRoad
        ufRoad.unite(a, b)
    for commandRail in commandsRail:
        a, b = commandRail
        ufRail.unite(a, b)
    d = collections.defaultdict(int)
    roots = []
    for i in range(1, N+1):
        roots.append((ufRoad.find(i), ufRail.find(i)))
        d[roots[i-1]] += 1
    print(*[d[root] for root in roots])

N, commandsRoad, commandsRail = getInputs()
solve(N, commandsRoad, commandsRail)
