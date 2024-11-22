import itertools
def get_inputs():
    N = int(input())
    As = []
    for _ in range(N):
        As.append(list(map(int, input().split())))
    M = int(input())
    XYgraph = [[] for _ in range(N)]
    for _ in range(M):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        XYgraph[x].append(y)
        XYgraph[y].append(x)
    return N, As, M, XYgraph
    
def solve():
    N, As, M, XYgraph = get_inputs()
    min_time = float("inf")
    for p in itertools.permutations(range(N)):
        ng = False
        for i in range(N-1):
            if p[i+1] in XYgraph[p[i]]:
                ng = True
                break
        if ng: continue
        time = sum([As[p[j]][j] for j in range(N)])
        if time < min_time:
            min_time = time
    if min_time == float("inf"):
        print(-1)
    else:
        print(min_time)

solve()