def get_inputs():
    H, W = map(int, input().split())
    As_all = []
    for _ in range(H):
        As_h = list(map(int, input().split()))
        As_all.append(As_h)
    Bs_all = []
    for _ in range(H):
        Bs_h = list(map(int, input().split()))
        Bs_all.append(Bs_h)
    return H, W, As_all, Bs_all


def solve():
    H, W, As, Bs = get_inputs()
    count = 0
    for y in range(H-1):
        for x in range(W-1):
            diff = Bs[y][x] - As[y][x]
            As[y+1][x] += diff
            As[y+1][x+1] += diff
            As[y][x] += diff
            As[y][x+1] += diff
            count += abs(diff)

    if all([As[H-1][x] == Bs[H-1][x] for x in range(W)] + [As[y][W-1] == Bs[y][W-1] for y in range(H)]):
        print("Yes")
        print(count)
    else:
        print("No")

solve()
