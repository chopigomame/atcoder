def solve():
    N = int(input())
    xs, ys = [], []
    for _ in range(N):
        x, y = map(int, input().split())
        xs.append(x)
        ys.append(y)
    xs.sort()
    ys.sort()

    if N % 2 == 0:
        median_x = (xs[(N-1)//2] + xs[(N-1)//2 + 1]) // 2
        median_y = (ys[(N-1)//2] + ys[(N-1)//2 + 1]) // 2
    else:
        median_x = xs[(N-1)//2]
        median_y = ys[(N-1)//2]
    
    cost = 0
    for i in range(N):
        x, y = xs[i], ys[i]
        cost += abs(median_x - x) + abs(median_y - y)
    print(cost)
    
solve()