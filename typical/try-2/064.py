def solve():
    N, Q = map(int, input().split())
    As = list(map(int, input().split()))
    deltas = [As[i+1] - As[i] for i in range(N-1)]
    E = sum([abs(e) for e in deltas])

    outs = []
    for _ in range(Q):
        L, R, V = map(int, input().split())
        L -= 1; R -= 1

        if L - 1 >= 0:
            new_delta = deltas[L - 1] + V
            E += abs(new_delta) - abs(deltas[L-1])
            deltas[L-1] = new_delta
        if R < N - 1:
            new_delta = deltas[R] - V
            E += abs(new_delta) - abs(deltas[R])
            deltas[R] = new_delta
        outs.append(E)
    
    print(*outs, sep="\n")

solve()
        