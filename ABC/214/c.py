import heapq


def get_inputs():
    N = int(input())
    Ss = list(map(int, input().split()))
    Ts = list(map(int, input().split()))
    graph = [[] for _ in range(N+1)] # 0 を高橋とする。 [cost, to] を入れる。
    graph[0] += [[t, i+1] for i, t in enumerate(Ts)]
    for i in range(N):
        curr = i + 1
        next = curr + 1
        if next == N + 1:
            next = 1
        graph[curr].append([Ss[i], next])
    return N, Ss, Ts, graph

def daikstra(start, graph):
    N = len(graph)
    inf = float("inf")

    dists = [inf for _ in range(N)]
    dists[start] = 0

    q = [[0, start]] # [dist, node]
    while q:
        dist, node = heapq.heappop(q)
        if dist > dists[node]:
            continue
        edges = graph[node]
        for cost, to in edges:
            new_dist = dists[node] + cost
            if new_dist < dists[to]:
                dists[to] = new_dist
                heapq.heappush(q, [new_dist, to])
    return dists
        
    
def solve():
    N, Ss, Ts, graph = get_inputs()
    dists = daikstra(0, graph)
    print(*dists[1:], sep="\n")
    
solve()


    