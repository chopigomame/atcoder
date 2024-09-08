def get_inputs():
    H, W, Q = map(int, input().split())
    bomb_graph = [[[ [h, w], [h, w], [h, w], [h, w] ] for w in range(W)] for h in range(H)]
    return H, W, Q, bomb_graph

def bomb(walls, bomb_graph, R, C, H, W):
    if walls[R][C] == 1:
        walls[R][C] = 0

        up =  R-1
        down = R+1
        left = C-1
        right = C+1
        bomb_graph[R, C] = [bomb_graph[up, C], bomb_graph[down, C], bomb_graph[R, left], bomb_graph[R, right]]
        return walls, bomb_graph
    else:
        for i in range(4):
            h, w = bomb_graph[R, C][i]
            while(True):
                if not (0 <= h < H and 0 <= w < W):
                    bomb_graph[R, C][i] = [h, w]
                    break
                if walls[h][w] == 0:
                    if i == 0:
                        h, w = bomb_graph[h, w][i]
                else:
                    walls[h][w] = 0
                    bomb_graph[R, C][i] = [h, w]
                    break

    return walls

def solve():
    H, W, Q, bomb_graph = get_inputs()
    walls = [[1] * W for _ in range(H)]
    for q in range(Q):
        R, C = map(int, input().split())
        R -= 1
        C -= 1
        walls = bomb(H, W, walls, R, C)
    summ = 0
    for h in walls:
        summ += sum(h)
    print(summ)
        

solve()
        