import math

def get_inputs():
    N = int(input())
    As = []
    for _ in range(N):
        As.append(list(map(int, input().split())))
    return N, As

def solve():
    N, As = get_inputs()
    print(math.prod([sum(A) for A in As]) % (10**9 + 7))


solve()