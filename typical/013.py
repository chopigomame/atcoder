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

# 練習のため、自分でベルマンフォードを考えてみる ⇒ 一応できた。が、確実に計算量で落ちる
def calc_min_costs(start, graph):
    INF = float("inf")
    ds = [INF] * len(graph)
    ds[start] = 0
    while(True):
        update = False
        for from_, edges in enumerate(graph):
            for cost, to in edges:
                if ds[from_] != INF and ds[to] > ds[from_] + cost:
                    ds[to] = ds[from_] + cost
                    update = True
        if not update:
            break
    return ds
                


def solve():
   N, M, graph = get_input() 
   costs_from_1 = calc_min_costs(0, graph)
   costs_from_N = calc_min_costs(N-1, graph)
   for k in range(N):
       print(costs_from_1[k] + costs_from_N[k])
       
solve()