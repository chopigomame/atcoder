def get_inputs():
    N, K = map(int, input().split())
    As = list(map(int, input().split()))
    return N, K, As

def solve():
    N, K, As = get_inputs()
    l = 0
    r = 0
    count = {}
    k = 0
    ans = 0
    for r in range(N):
        count.setdefault(As[r], 0)
        count[As[r]] += 1
        if count[As[r]] == 1:
            k += 1

        while(k > K):
            count[As[l]] -= 1
            if count[As[l]] == 0:
                k -= 1
            l += 1
        
        ans = max(ans, r - l + 1)
    
    print(ans)

solve()