import bisect
def get_inputs():
    N = int(input())
    Xs = []
    Ys = []
    for _ in range(N):
        X, Y = map(int, input().split())
        Xs.append(X)
        Ys.append(Y)
    return N, Xs, Ys

def solve():
    def dist(x, xs):
        return sum([abs(x_ - x) for x_ in xs])
    
    def bisect(start, end, xs):
        while( end-start > 1):
            mid = start + (end - start) // 2
            d_plus = dist(mid, xs)
            d_minus = dist(mid-1, xs)
            if d_plus <= d_minus:
                start = mid
            else:
                end = mid-1 
        if dist(start, xs) <= dist(end, xs):
            return start
        else:
            return end

    N, Xs, Ys = get_inputs()
    s = -(10**9)
    e = 10**9

    x = bisect(s, e, Xs)
    y = bisect(s, e, Ys)
    
    print(dist(x, Xs) + dist(y, Ys))

solve()