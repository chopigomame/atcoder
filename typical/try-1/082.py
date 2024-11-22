def solve():
    L, R = map(int, input().split())
    orig_L, orig_R = L, R
    d = {}
    for i in range(18):
        if L > 10**(i+1):
            continue
        d[i] = min(R, 10**(i+1) - 1) - L + 1
        L = 10**(i+1)
        if R < L:
            break
    
    count = 0
    mod = 10 ** 9 + 7
    for i in d.keys():
        s = max(10**i, orig_L) - 1
        e = min(10**(i+1) - 1, orig_R)
        num = (e * (e + 1) // 2) - (s * (s + 1) // 2)
        count += num * (i+1)
    print(int(count % mod))

solve()
        