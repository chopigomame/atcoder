import sys
sys.setrecursionlimit(10**6)

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

    seen = [False for _ in range(N)]
    ans = []
    def dfs(curr_node):
        seen[curr_node] = True
        edges = sorted(graph[curr_node])
        ans.append(curr_node + 1)

        for edge in edges:
            if not seen[edge]:
                dfs(edge)
                ans.append(curr_node + 1)

    dfs(0)
    
    print(*ans)

solve()