import bisect
def solve():
    N = int(input())
    As = list(map(int, input().split()))
    As.sort()
    Q = int(input())
    for q in range(Q):
        b = int(input())
        i = bisect.bisect_left(As, b)
        if i == 0:
            print(As[i] - b)
        elif i == N:
            print(b - As[N-1])
        else:
            print(min(As[i] - b, b - As[i-1]))

solve()