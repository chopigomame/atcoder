def mod_pow(base, power, mod):
    if base <= 0:
        return 0
    base %= mod
    n = 1
    ans = 1
    while(power > 0):
        if n > power:
            base = base ** (1/2)
            n //= 2
        else:
            power -= n
            ans = (ans * base) % mod
            base = (base ** 2) % mod
            n *= 2

    return ans

def mod_pow(base, power, mod):
    if base <= 0 or mod <= 0:
        return 0  # モジュロは正である必要がある

    base %= mod  # base を mod で最初に正規化
    ans = 1

    while power > 0:
        # power が奇数の場合、結果に base を掛ける
        if power % 2 == 1:
            ans = (ans * base) % mod
        
        # base を2乗し、power を半分にする
        base = (base * base) % mod
        power //= 2

    return ans

def solve():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    ans = 1
    for n in range(N):
        if n == 0:
            ans *= K
        elif n == 1:
            ans *= K-1
        else:
            ans *= mod_pow(K-2, N-2, MOD)
            ans %= MOD
            break
    print(ans)

solve()