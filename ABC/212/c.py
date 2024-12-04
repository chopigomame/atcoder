import bisect
def solve():
    N, M = map(int, input().split())
    As = sorted(list(map(int, input().split())))
    Bs = sorted(list(map(int, input().split())))

    min_diff = float("inf")
    for A in As:
        idx = bisect.bisect_left(Bs, A)
        if idx == 0:
            min_diff = min(min_diff, abs(A-Bs[idx]))
        elif idx == M:
            min_diff = min(min_diff, abs(A-Bs[M-1]))
        else:
            min_diff = min(min_diff, abs(A-Bs[idx]), abs(A-Bs[idx-1]))
    print(min_diff)

solve()