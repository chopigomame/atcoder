import bisect

def get_inputs():
    N = int(input())
    Xs = list(map(int, input().split()))
    Ps = list(map(int, input().split()))
    return N, Xs, Ps

def solve():
    N, Xs, Ps = get_inputs()
    Xs = [-float("inf")] + Xs
    Ps = [0] + Ps
    summs = {}
    prev = 0
    for i, x in enumerate(Xs):
        summs[x] = prev + Ps[i]
        prev = summs[x]
    
    Q = int(input())
    for q in range(Q):
        l, r = map(int, input().split())
        
        l_idx = bisect.bisect_right(Xs, l - 1) - 1
        r_idx = bisect.bisect_left(Xs, r + 1) - 1
        l_x, r_x = Xs[l_idx], Xs[r_idx]

        print(summs[r_x] - summs[l_x])

solve()
        