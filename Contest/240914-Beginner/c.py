import itertools

def get_inputs():
    N = int(input())
    Mg = int(input())
    graph_g = [[0 for _ in range(N)] for _ in range(N)]
    for mg in range(Mg):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph_g[a][b] = 1
        graph_g[b][a] = 1
    Mh = int(input())
    graph_h = [[0 for _ in range(N)] for _ in range(N)]
    for mg in range(Mh):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph_h[a][b] = 1
        graph_h[b][a] = 1
    As = []
    for i in range(N-1):
        As.append([0] * (i+1) + list(map(int, input().split())))
    return N, graph_g, graph_h, As

def solve():
    N, graph_g, graph_h, As = get_inputs()

    min_cost = float("inf")
    for perm in itertools.permutations(list(range(N))):
        corres_perm = [perm.index(i) for i in range(N)]
        new_graph_g = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                new_graph_g[i][corres_perm[j]] = graph_g[perm[i]][j]
        
        cost = 0
        for i in range(N-1):
            for j in range(i+1, N):
                if new_graph_g[i][j] != graph_h[i][j]:
                    cost += As[i][j]
        if cost < min_cost:
            min_cost = cost
    print(min_cost)

solve()