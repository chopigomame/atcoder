def get_inputs():
    H, W = map(int, input().split())
    Q = int(input())
    return H, W, Q

def solve():
    H, W, Q = get_inputs()
    box = [[0 for _ in range(W)] for _ in range(H)]
    ds = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    groups = []

    for _ in range(Q):
        query = list(map(int, input().split()))
        q = query[0]
        if q == 1:
            r, c = query[1:]
            r, c = r-1, c-1
            box[r][c] = 1
            tonari_group = set()
            for dy, dx in ds:
                tonari = (r + dy, c + dx)
                for group in groups:
                    if not tonari in group:
                        continue
                    tonari_group = tonari_group | group
                    groups.remove(group)
            tonari_group.add((r, c))
            groups.append(tonari_group)
                    
        else:
            ra, ca, rb, cb = query[1:]
            ra, ca, rb, cb = ra-1, ca-1, rb-1, cb-1
            found = False
            for group in groups:
                if (ra, ca) in group and (rb, cb) in group:
                    found = True
            if found:
                print("Yes")
            else:
                print("No")

solve()