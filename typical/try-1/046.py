def get_inputs():
    N = int(input())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))
    Cs = list(map(int, input().split()))
    return N, As, Bs, Cs

def solve():
    N, As, Bs, Cs = get_inputs()
    AsAmari = {i:0 for i in range(46)}
    BsAmari = {i:0 for i in range(46)}
    CsAmari = {i:0 for i in range(46)}
    for Xs, XsAmari in zip([As, Bs, Cs], [AsAmari, BsAmari, CsAmari]):
        for e in Xs:
            XsAmari[e%46] += 1
    count = 0
    for a in range(0, 46):
        for b in range(0, 46):
            for c in range(0, 46):
                if (a + b + c) % 46 == 0:
                    count += AsAmari[a] * BsAmari[b] * CsAmari[c]
    print(count)

solve()