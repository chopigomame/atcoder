def get_inputs():
    N = int(input())
    papers = []
    for _ in range(N):
        lx, ly, rx, ry = map(int, input().split())
        papers.append([lx, ly, rx, ry])
    return N, papers

def solve():
    N, papers = get_inputs()
    SIZE = 1000
    box = [[0 for _ in range(SIZE+1)] for _ in range(SIZE+1)]

    for paper in papers:
        lx, ly, rx, ry = paper
        box[lx][ly] += 1
        box[rx][ly] -= 1
        box[rx][ry] += 1
        box[lx][ry] -= 1

    # 横方向の和
    for h in range(SIZE):
        accum = 0
        for w in range(SIZE):
            accum += box[h][w]
            box[h][w] = accum
    # 縦方向の和
    for w in range(SIZE):
        accum = 0
        for h in range(SIZE):
           accum += box[h][w]
           box[h][w] = accum

    totals = {n:0 for n in range(N+1)}
    for w in range(SIZE):
        for h in range(SIZE):
            val = box[h][w]
            totals[val] += 1
    
    for n in range(1, N+1):
        print(totals[n])

solve()