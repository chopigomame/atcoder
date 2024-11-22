def get_inputs():
    N = int(input())
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    return N, graph

def solve():
    N, graph = get_inputs()
    evens = [1]
    odds = []
    prev_nodes = [0]
    next_nodes = graph[0]
    d = 0
    while(next_nodes):
        d += 1
        new_next_nodes = []
        for node in next_nodes:
            if d%2 == 0:
                evens.append(node + 1)
            else:
                odds.append(node + 1)
            new_next_nodes.extend([e for e in graph[node] if not e in prev_nodes])

        prev_nodes = next_nodes
        next_nodes = new_next_nodes
    if len(evens) >= N//2:
        print(*evens[:N//2], sep=" ")
    else:
        print(*odds[:N//2], sep=" ")

solve()