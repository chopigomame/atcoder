def solve():
    N, K = map(int, input().split())
    As, Bs = [], []
    for _ in range(N):
        a, b = map(int, input().split())
        As.append(a)
        Bs.append(b)

    scores = sorted(Bs + [As[i] - Bs[i] for i in range(N)], reverse=True)
    print(sum(scores[:K]))
solve()
        