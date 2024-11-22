def solve():
    N, K = map(int, input().split())
    S = input()

    LRs = []
    
    continueing = False
    for i, s in enumerate(S + "0"):
        if not continueing and s == "1":
            l = i
            continueing = True
        if continueing and s == "0":
            r = i - 1
            LRs.append([l, r])
            continueing = False
    
    K -= 1
    S1 = S[0 : LRs[K-1][1] + 1]
    S2 = S[LRs[K][0] : LRs[K][1]+1]
    S3 = S[LRs[K-1][1] + 1 : LRs[K][0]]
    S4 = S[LRs[K][1] + 1:]
    
    print(S1 + S2 + S3 + S4)

solve()