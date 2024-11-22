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
    
    depths = [-1 for _ in range(N)]
    depths[0] = 0
    even_nodes = [1]
    odd_nodes = []

    q = queue.Queue()
    q.put(0)
    while(not q.empty()):
        pv = q.get()
        for to_v in graph[pv]:
            if depths[to_v] != -1:
                continue
            depths[to_v] = depths[pv] + 1
            if depths[to_v] % 2 == 0:
                even_nodes.append(to_v+1)
            else:
                odd_nodes.append(to_v+1)
            q.put(to_v)
    if len(even_nodes) >= len(odd_nodes):
        print(*even_nodes[:N//2])
    else:
        print(*odd_nodes[:N//2])

solve()
            

            
