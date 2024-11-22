def solve():
    N = int(input())
    S = input()
    
    memos = {"o": [], "x": []}
    for i, s in enumerate(S):
        memos[s].append(i)

    first_idxes = {s: 0 for s in ["o", "x"]}
    lookup = {"o": "x", "x": "o"}
    count = 0
    for i, s in enumerate(S):
        try:
            count += N - memos[lookup[s]][first_idxes[lookup[s]]]
            first_idxes[s] += 1
        except:
            continue
    print(count)

solve()