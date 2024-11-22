import math

def get_inputs():
    N, L = map(int, input().split())
    return N, L

def solve():
    N, L = get_inputs()
    count = 0
    for n_l in range(0, (N//L)+1):
        T = n_l + (N - L * n_l)
        count += math.comb(T, n_l)
    print(count % (10**9 + 7))

solve()