def solve():
    N, M = map(int, input().split())
    graph = [[-1 for _ in range(N)] for _ in range(N)]
    ans = [[-1 for _ in range(N)] for _ in range(N)]
    count = 0

    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1; b -= 1
        graph[a][b] = 1
        if graph[b][a] == 1:
            if ans[max(a, b)][min(a, b)] != 1:
                ans[max(a, b)][min(a, b)] = 1
                count += 1
    print(count)

solve()
