def get_inputs():
    N = int(input())
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        a, b = a-1, b-1
        graph[a].append(b)
        graph[b].append(a)
    return N, graph

def find_farest(i, graph):
    nexts = [e for e in graph[i]]
    seen = {i}
    dist = 0
    while(len(nexts)>0):
        new_nexts = []
        for next in nexts:
            if next in seen: continue
            seen.add(next)

            new_nexts.extend(graph[next])
            farest = next
        nexts = new_nexts
        dist += 1
    return farest, dist

def solve():
    N, graph = get_inputs()
    farest_1, _ = find_farest(0, graph)
    farest_2, dist = find_farest(farest_1, graph)
    print(dist)

solve()
    