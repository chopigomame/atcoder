import bisect

def get_inputs():
    N, K = map(int, input().split())
    As  = list(map(int, input().split()))
    return N, K, As

def solve():
    N, K, As = get_inputs()
    l, r = -1, -1

    s = dict()
    mm = 0
    while l<N:
        if len(s) <= K and r<N:
            mm = max(mm, r-l)
            r += 1
            if r<N:
                s[As[r]] = s.get(As[r], 0) + 1
        else:
            l += 1
            if l<N:
                s[As[l]] = s[As[l]] - 1
                if s[As[l]] == 0:
                    s.pop(As[l])
    print(mm)

solve()