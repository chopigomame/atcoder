def get_inputs():
    H, W = map(int, input().split())
    cs = []
    for _ in range(H):
        cs.append(list(input()))
    return H, W, cs

max_dist = 0
def solve():
    
    def find_active_direction(point, distance):
        global max_dist
        py, px = point
        seen[py][px] = 1
        for dy, dx in ds:
            ny, nx = py + dy, px + dx
            if start == (ny, nx):
                max_dist = max(max_dist, distance + 1)
                continue
            if not (0 <= ny < H and 0 <= nx < W and cs[ny][nx] == "." and seen[ny][nx] == 0):
                continue
            find_active_direction([ny, nx], distance + 1)
        seen[py][px] = 0
        

    H, W, cs = get_inputs()
    seen = [[0 for _ in range(W)] for _ in range(H)]
    ds = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for h in range(H):
        for w in range(W):
            if cs[h][w] == "#":
                continue
            start = (h, w)
            find_active_direction(start, 0)
            
    if max_dist < 3:
        print(-1)
    else:
        print(max_dist)

solve()