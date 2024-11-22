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
    if N > 0:
        ans *= pow(K-2, N, 10**9+7)
    print(ans)

solve()