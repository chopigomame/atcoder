def get_inputs():
    N = int(input())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))
    return N, As, Bs

def solve():
    N, As, Bs = get_inputs()
    As.sort()
    Bs.sort()
    E = 0
    for i in range(N):
        E += abs(As[i] - Bs[i])
    print(E)

solve()