def solve():
    N = int(input())
    As = sorted(list(map(int, input().split())))
    Bs = sorted(list(map(int, input().split())))

    cost = sum([abs(As[i] - Bs[i]) for i in range(N)])
    print(cost)

solve()