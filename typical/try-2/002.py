import itertools
def solve():
    N = int(input())
    for pars in itertools.product(["(", ")"], repeat=N):
        pars = "".join(pars)
        score = 0
        ok = True
        for p in pars:
            if p == "(":
                score += 1
            else:
                score -= 1
            if score < 0:
                ok = False
                break
        if score != 0:
            ok = False
        if ok:
            print(pars)

solve()