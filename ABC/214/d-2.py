from typing import List, Dict

class UnionFind():
    # 初期化
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n

    # 根を求める
    def root(self, x):
        if self.par[x] == -1: return x # x が根の場合は x を返す
        else:
          self.par[x] = self.root(self.par[x]) # 経路圧縮
          return self.par[x]

    # x と y が同じグループに属するか (根が一致するか)
    def issame(self, x, y):
        return self.root(x) == self.root(y)

    # x を含むグループと y を含むグループを併合する
    def unite(self, x, y):
        # x 側と y 側の根を取得する
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry: return False # すでに同じグループのときは何もしない
        # union by rank
        if self.rank[rx] < self.rank[ry]: # ry 側の rank が小さくなるようにする
            rx, ry = ry, rx
        self.par[ry] = rx # ry を rx の子とする
        if self.rank[rx] == self.rank[ry]: # rx 側の rank を調整する
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry] # rx 側の siz を調整する
        return True
    
    # x を含む根付き木のサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]

def get_inputs():
    N = int(input())
    nodes_for_w = {}
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        nodes_for_w.setdefault(w, [])
        nodes_for_w[w].append((u, v))
    
    return N, nodes_for_w

def solve():
    N, nodes_for_w = get_inputs()
    uf = UnionFind(N)
    ws = sorted(nodes_for_w.keys())
    ans = 0
    for w in ws:
        for n1, n2 in nodes_for_w[w]:
            # s1 = max(uf.size(n1)-1 , 0)
            # s2 = max(uf.size(n2)-1 , 0)
            # ans += (s1 + s2 + 1) * w
            s1 = uf.size(n1)
            s2 = uf.size(n2)
            ans += s1 * s2 * w
            uf.unite(n1, n2)
    print(ans)
    
solve()