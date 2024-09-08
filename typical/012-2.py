import collections
class UnionFind():
    def __init__(self):
        '''
        unionfind経路圧縮あり,要素にtupleや文字列可,始めに要素数指定なし
        '''
        self.parents = dict()                                      # {子要素:親ID,}
        self.members_set = collections.defaultdict(lambda : set()) # keyが根でvalueが根に属する要素要素(tupleや文字列可)
        self.roots_set = set()                                     # 根の集合(tupleや文字列可)
        self.key_ID = dict()                                       # 各要素にIDを割り振る
        self.ID_key = dict()                                       # IDから要素名を復元する
        self.cnt = 0                                               # IDのカウンター

    def dictf(self,x): # 要素名とIDをやり取りするところ
        if x in self.key_ID:
            return self.key_ID[x]
        else:
            self.cnt += 1
            self.key_ID[x] = self.cnt
            self.parents[x] = self.cnt
            self.ID_key[self.cnt] = x
            self.members_set[x].add(x)
            self.roots_set.add(x)
            return self.key_ID[x]

    def find(self, x):
        ID_x = self.dictf(x)
        if self.parents[x] == ID_x:
            return x
        else:
            self.parents[x] = self.key_ID[self.find(self.ID_key[self.parents[x]])]
            return self.ID_key[self.parents[x]]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        if x == y:
            return
        for i in self.members_set[y]:
            self.members_set[x].add(i)
        self.members_set[y] = set()
        self.roots_set.remove(y)
        self.parents[y] = self.key_ID[x]

    def size(self, x):#xが含まれる集合の要素数
        return len(self.members_set[self.find(x)])

    def same(self, x, y):#同じ集合に属するかの判定
        return self.find(x) == self.find(y)

    def members(self, x):#xを含む集合の要素
        return self.members_set[self.find(x)]

    def roots(self):#根の要素
        return self.roots_set

    def group_count(self):#根の数
        return len(self.roots_set)

    def all_group_members(self):#根とその要素
        return {r: self.members_set[r] for r in self.roots_set}

def get_inputs():
    H, W = map(int, input().split())
    Q = int(input())
    return H, W, Q

def get_query():
    inp = input()
    if inp[0] == "1":
        t, r, c = map(int, inp.split(" "))
        return t, r-1, c-1
    elif inp[0] == "2":
        t, ra, ca, rb, cb  = map(int, inp.split(" "))
        return t, ra-1, ca-1, rb-1, cb-1
    
def solve():
    H, W, Q = get_inputs()
    cells = [[0] * W for _ in range(H)]
    uf = UnionFind()
    for q in range(Q):
        query = get_query()
        if query[0] == 1:
            r, c = query[1:]
            cells[r][c] = 1
            for dx, dy in ([-1, 0], [0, 1], [1, 0], [0, -1]):
                nr, nc = r + dx, c + dy
                if 0 <= nr < H and 0 <= nc < W and cells[nr][nc] == 1:
                    uf.union((r, c), (nr, nc))
        else:
            ra, ca, rb, cb = query[1:]
            if cells[ra][ca] == 1 and cells[rb][cb] == 1 and uf.find((ra, ca)) == uf.find((rb, cb)):
                print("Yes")
            else:
                print("No")
solve()
                    
