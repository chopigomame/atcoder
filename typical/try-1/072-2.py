from itertools import product
import itertools
def get_inputs():
    H, W = map(int, input().split())
    cs = []
    for _ in range(H):
        cs.append(list(input()))
    return H, W, cs

ans = 0
def solve():
    ds = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def dfs(s, map, seen):
        global ans 

        cy, cx = s
        seen[cy][cx] = True
        for dy, dx in ds:
            ny, nx = cy + dy, cx + dx

            if (ny, nx) == origin:
                summ = sum([sum(e) for e in seen])
                if summ > ans:
                    ans = summ
                continue

            if not 0 <= ny < H or not 0 <= nx < W:
                continue
            if map[ny][nx] == "#" or seen[ny][nx]:
                continue

            dfs((ny, nx), map, seen)

        seen[cy][cx] = False

    H, W, cs = get_inputs()
    seen = [[False for _ in range(W)] for _ in range(H)]
    for y in range(H):
        for x in range(W):
            origin = (y, x)
            if cs[y][x] == "#":
                continue
            dfs(origin, cs, seen)
    
    if ans <= 2:
        print(-1)
    else:
        print(ans)
            
    
    
solve()