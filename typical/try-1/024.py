def get_inputs():
    N, K = map(int, input().split())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))
    return N, K, As, Bs


def solve():
    N, K, As, Bs = get_inputs()
    d = 0
    for n in range(N):
        d += abs(As[n] - Bs[n])
    if K - d >= 0 and (K - d)%2 == 0:
        print("Yes")
    else:
        print("No")

solve()