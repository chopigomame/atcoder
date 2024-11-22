def solve():
    K_str = input()
    if sum([int(e) for e in list(K_str)]) % 9 != 0:
        print(0)
        return

    K = int(K_str)
    DP = [0 for _ in range(K+1)]
    DP[0] = 1
    for k in range(K+1):
        for i in range(1, 10):
            if k - i >= 0:
                DP[k] += DP[k - i]
    print(DP[K] % (10**9 + 7))

solve()