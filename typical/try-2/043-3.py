from collections import deque
def get_inputs():
    H, W = map(int, input().split())
    rs, cs = [e-1 for e in list(map(int, input().split()))]
    rt, ct = [e-1 for e in list(map(int, input().split()))]
    Ss = []
    for _ in range(H):
        Ss.append(list(input()))
    return H, W, rs, cs, rt, ct, Ss

def solve():
    H, W, rs, cs, rt, ct, Ss = get_inputs()

    INF = float("inf")
    DP = [
        [
            [INF for _ in range(4)] for _ in range(W)
        ] for _ in range(H)
    ]
    DP[rs][cs] = [0, 0, 0, 0]

    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    q = deque()
    for i in range(4):
        q.append([0, rs, cs, i])

    while(q):
        d, r, c, i = q.popleft()
        if d > DP[r][c][i]:
            continue
        dy, dx = directions[i]
        nr, nc = r + dy, c + dx
        if not (0 <= nr < H and 0 <= nc < W and Ss[nr][nc] == "."):
            continue

        if DP[r][c][i] < DP[nr][nc][i]:
            DP[nr][nc][i] = DP[r][c][i]
            q.appendleft([DP[nr][nc][i], nr, nc, i])
            for j in range(4):
                if DP[nr][nc][i] + 1 < DP[nr][nc][j]:
                    DP[nr][nc][j] = DP[nr][nc][i] + 1
                    q.append([DP[nr][nc][j], nr, nc, j])
    print(min(DP[rt][ct]))

solve()
        