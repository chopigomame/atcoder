def solve():
    L, R = map(int, input().split())
    count = 0
    mod = 10 ** 9 + 7
    min_order = len(str(L)) - 1
    max_order = len(str(R)) - 1
    for i in range(min_order, max_order+1):
        s = max(10**i, L)
        e = min(10**(i+1) - 1, R)
        num = e - s + 1
        count_i = (s + e) * num // 2
        count += count_i * (i+1)
        
    print(int(count % mod))

solve()