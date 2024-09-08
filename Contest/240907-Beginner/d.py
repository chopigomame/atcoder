def get_inputs():
    H, W, Q = map(int, input().split())
    return H, W, Q

def bomb(H, W, walls, R, C):
    if walls[R][C] == 1:
        walls[R][C] = 0
        return walls
    for r in range(R, -1, -1):
        if walls[r][C] == 1:
            walls[r][C] = 0
            break
    for r in range(R, H):
        if walls[r][C] == 1:
            walls[r][C] = 0
            break
    for c in range(C, -1, -1):
        if walls[R][c] == 1:
            walls[R][c] = 0
            break
    for c in range(C, W):
        if walls[R][c] == 1:
            walls[R][c] = 0
            break
    return walls

def solve():
    H, W, Q = get_inputs()
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
        