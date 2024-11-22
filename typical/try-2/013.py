import heapq

def get_inputs():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append((c, b)) # cost, to
        graph[b].append((c, a)) # cost, to
    return N, M, graph

def daikstra(s, graph):
    q = [(0, s)] # current_cost, node
    dist = [float("inf") for _ in range(len(graph))]
    dist[s] = 0
    while q:
        d, node = heapq.heappop(q)
        if d > dist[node]:
            continue
        edges = graph[node]
        for cost, to in edges:
            if cost + d < dist[to]:
                dist[to] = cost + d
                heapq.heappush(q, (cost + d, to))
    return dist


def solve():
    N, M, graph = get_inputs()
    dist_from_1 = daikstra(0, graph)
    dist_from_N = daikstra(N-1, graph)

    for k in range(N):
        print(dist_from_1[k] + dist_from_N[k])

solve()

    
