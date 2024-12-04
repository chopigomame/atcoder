def solve():
    N, D = map(int, input().split())
    S = input()
    
    S_reverse = list(S[::-1])
    for _ in range(D):
        idx = S_reverse.index("@")
        S_reverse[idx] = "."
        
    print("".join(S_reverse[::-1]))
    
solve()
