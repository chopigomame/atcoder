from itertools import product
import itertools
def get_inputs():
    H, W = map(int, input().split())
    cs = []
    for _ in range(H):
        cs.append(list(input()))
    return H, W, cs

def solve():
    H, W, cs = get_inputs()
    max_num = -1

    for p in product([0, 1], repeat=H*W):

        active_map = [[0 for _ in range(W)] for _ in range(H)]
        active_points = [[x//W, x%W] for x, v in enumerate(p) if v == 1]

        for ap in active_points:
            if cs[ap[0]][ap[1]] == "#":
                continue
            active_map[ap[0]][ap[1]] = 1
        
        num = 0
        for yx in product(range(H), range(W)):
            y, x = yx
            if active_map[y][x] != 1:
                continue

            adj_count = 0
            for dy, dx in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                _y, _x = y + dy, x + dx
                if (0 <= _y < H) and (0 <= _x < W) and active_map[_y][_x]:
                    adj_count += 1
            if adj_count == 2:
                num += 1
            else:
                num = 0
                break
        if num > max_num:
            max_num = num

    if max_num == 0:
        print(-1)
    else:
        print(max_num)
solve()