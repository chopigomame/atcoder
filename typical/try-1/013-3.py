import heapq

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

# 練習のため、自分でダイクストラを考えてみる heapqを使う
def calc_min_costs(start, graph):
    INF = float("inf")
    ds = [INF] * len(graph)
    ds[start] = 0
    used_flags = [False] * len(graph)
    q = [[0, start]]

    while(q):
        v = heapq.heappop(q)[1]
        if used_flags[v] == True:
            continue
        used_flags[v] = True

        edges = graph[v]
        for cost, to in edges:
            if ds[to] > ds[v] + cost:
                ds[to] = ds[v] + cost
                heapq.heappush(q, [ds[to], to])
    return ds


def solve():
   N, M, graph = get_input() 
   costs_from_1 = calc_min_costs(0, graph)
   costs_from_N = calc_min_costs(N-1, graph)
   for k in range(N):
       print(costs_from_1[k] + costs_from_N[k])
       
solve()