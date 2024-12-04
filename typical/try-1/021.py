import sys
sys.setrecursionlimit(100000)

curr_label = 0

def solve():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    reverse_graph = [[] for _ in range(N)]

    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1; b -= 1
        graph[a].append(b)
        reverse_graph[b].append(a)
        
    
    labels = [-1 for _ in range(N)]
    def dfs(curr_node, graph):
        global curr_label
        labels[curr_node] = 0
        for to in graph[curr_node]:
            if labels[to] == -1:
                dfs(to, graph)
        labels[curr_node] = curr_label
        curr_label += 1
        
    for i, label in enumerate(labels):
        if label == -1:
            dfs(i, graph)
    labels_with_index = sorted(list(enumerate(labels)), key=lambda x:x[1], reverse=True)
    
    SCCs = []
    seens = [-1 for _ in range(N)]
    
    def dfs2(curr_node, graph):
        seens[curr_node] = 1
        SCC.append(curr_node)
        for to in graph[curr_node]:
            if seens[to] == -1:
                dfs2(to, graph)
    
    ans = 0
    for i, _ in labels_with_index:
        if seens[i] == -1:
            SCC = []
            dfs2(i, reverse_graph)
            SCCs.append(SCC)
            ans += (len(SCC) * (len(SCC) - 1)) // 2
    
    print(ans)
            
solve()
