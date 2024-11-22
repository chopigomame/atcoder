def solve():
    S = input()
    sp = S.split("|")
    counts = []
    for s in sp[1:-1]:
        counts.append(s.count("-"))
    print(*counts)
solve()