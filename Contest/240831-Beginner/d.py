def get_inputs():
    N = int(input())
    As = list(map(int, input().split()))
    return N, As

def solve():
    N, As = get_inputs()
    DP = [[-1, -1] for _ in range(N+1)]
    DP[0] = [0, -As[0]*2]
    for i, a in enumerate(As, 1):
        DP[i][0] = max(DP[i-1][0], DP[i-1][1] + a*2)
        DP[i][1] = max(DP[i-1][0] + a, DP[i-1][1])
    print(max(DP[N]))

solve()