def get_inputs():
    N, K = map(int, input().split())
    return N, K

def solve():
    N, K = get_inputs()
    ans = 1
    for i in range(N):
        if i == 0:
            ans *= K
        elif i == 1:
            ans *= (K-1)
        else:
            break
    N -= 2
    n = 1
    ks = {1:K-2}
    k = ks[1]
    mod = 10**9 + 7
    while(N>0):
        if k == 0:
            ans = 0
            break
        if N >= n:
            ans = ans * k % mod
            N -= n
            n *= 2
            try:
                k = ks[n]
            except:
                k **= 2
                ks[n] = k
        else:
            while(N < n):
                n //= 2
                k = ks[n]
    print(ans % (10**9 + 7))

solve()