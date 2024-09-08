def get_inputs():
    N = int(input())
    As = []
    for _ in range(N):
        As.append(list(map(int, input().split())))
    return N, As

def solve():
    N, As = get_inputs()
    curr = 0
    for n in range(N):
        if curr >= n:
            curr = As[curr][n] - 1 
        else:
            curr = As[n][curr] - 1
    print(curr+1)
    
solve()