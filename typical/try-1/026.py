import queue
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
    for i, edges in enumerate(graph):
        if len(edges) == 1:
            start = i
            break
    
    used_nodes = [-1 for _ in range(N)]
    ret = []

    q = queue.Queue()
    q.put(start)
    while(not q.empty()):
        cv = q.get()
        used_nodes[cv] = 1

        edges = []
        for e in graph[cv]:
            if used_nodes[e] != 1:
                edges.append(e)

        for e in edges:
            _edges = []
            for e2 in graph[e]:
                if used_nodes[e2] != 1:
                    _edges.append(e2)
            if len(_edges) >= 2:
                q.put(e)
            else:
                ret.append(e+1)
                used_nodes[e] = 1
                for _e in _edges:
                    q.put(_e)
    print(*ret[:N//2])

solve()
            

            
