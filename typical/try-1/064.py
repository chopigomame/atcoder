def get_inputs():
    N, Q = map(int, input().split())
    As = list(map(int, input().split()))
    return N, Q, As

def solve():
    N, Q, As = get_inputs()
    Cs = [As[i] - As[i+1] for i in range(N-1)]
    summ = sum([abs(c) for c in Cs])
    summs = []
    for q in range(Q):
        L, R, V = map(int, input().split())
        L-=1; R-=1
        if L != 0:
            prev = Cs[L-1]
            Cs[L-1] -= V
            summ += abs(Cs[L-1]) - abs(prev)
        if R <= N-2:
            prev = Cs[R]
            Cs[R] += V
            summ += abs(Cs[R]) - abs(prev)
        summs.append(summ)
    print(*summs, sep="\n")

solve()