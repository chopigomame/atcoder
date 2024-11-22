def solve():
    H, W = map(int, input().split())
    if H < 2 or W < 2:
        print(H*W)
    else:
        print((W // 2 + W % 2) * (H // 2 + H % 2))
solve()