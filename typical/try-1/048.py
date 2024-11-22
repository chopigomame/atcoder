def get_inputs():
    N, K = map(int, input().split())
    ABs = [[]]
    for _ in range(N):
        ABs.append(list(map(int, input().split())))
    return N, K, ABs

def solve():
    N, K, ABs = get_inputs()
    DPs = [[0]*(K+1) for _ in range(N+1)]
    for n in range(1, N+1):
        for k in range(0, K+1):
            cand = []
            if k-1 >= 0:
                cand.append(DPs[n-1][k-1] + ABs[n][1])
            if k-2 >= 0:
                cand.append(DPs[n-1][k-2] + ABs[n][0])
            cand.append(DPs[n-1][k])
            DPs[n][k] = max(cand)
    print(max(DPs[N]))

solve()