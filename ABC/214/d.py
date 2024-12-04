import heapq

def get_inputs():
    N = int(input())
    graph = [{i:0} for i in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        graph[u][v] = w
        graph[v][u] = w
    return N, graph

def daikstra(start, graph):
    N = len(graph)
    inf = float("inf")
    dists = [inf for _ in range(N)]
    dists[start] = 0
    F = [0 for _ in range(N)]

    q = [[0, start, start, 0, 0]] # [dist, node, prev_node, max_weight, count]
    while q:
        dist, node, prev_node, max_weight, count = heapq.heappop(q)
        if dist > dists[node]:
            continue
        edges = graph[node]
        curr_weight = edges[prev_node]
        print("m, c:", max_weight , curr_weight)
        if max_weight < curr_weight:
            print("a")
            max_weight = curr_weight
            F[node] = max_weight * count
        else:
            print("b")
            F[node] = F[prev_node] + curr_weight
        for to in edges.keys():
            cost = edges[to]
            new_dist = dists[node] + cost
            if new_dist < dists[to]:
                dists[to] = new_dist
                heapq.heappush(q, [new_dist, to, node, max_weight, count+1])
    return F
        
    
def solve():
    N, graph = get_inputs()
    for node in range(N):
        if len(graph[node]) == 2:
            start = node
            break

    ans = 0
    F = daikstra(start, graph)
    print(F)
    print(sum(F))
    
solve()


    