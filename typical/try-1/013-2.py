def get_input():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append([c, b])
        graph[b].append([c, a])
    return N, M, graph

# 練習のため、自分でダイクストラを考えてみる
def calc_min_costs(start, graph):
    INF = float("inf")
    ds = [INF] * len(graph)
    ds[start] = 0
    used_flags = [False] * len(graph)

    while(True):
        # 起点となるノードの選定
        min_d = INF
        next = -1
        for i, d in enumerate(ds):
            if not used_flags[i] and d < min_d:
                min_d = d
                next = i
        if next == -1:
            break
        used_flags[next] = True

        edges = graph[next]
        for cost, to in edges:
            if ds[to] > ds[next] + cost:
                ds[to] = ds[next] + cost
    return ds


def solve():
   N, M, graph = get_input() 
   costs_from_1 = calc_min_costs(0, graph)
   costs_from_N = calc_min_costs(N-1, graph)
   for k in range(N):
       print(costs_from_1[k] + costs_from_N[k])
       
solve()