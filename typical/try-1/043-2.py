import queue
def get_inputs():
    H, W = map(int, input().split())
    rs, cs = map(int, input().split())
    rt, ct = map(int, input().split())
    box = []
    for _ in range(H):
        box.append(list(input()))
    return (rs-1, cs-1), (rt-1, ct-1), box, H, W


def solve():
    s, t, box, H, W = get_inputs()
    INF = 10 ** 10
    scores = [[[INF for _ in range(4)] for _ in range(W)] for _ in range(H)]
    scores[s[0]][s[1]] = [0, 0, 0, 0]

    q = queue.Queue()
    for d in range(4):
        q.put([s, d, 0]) # [位置, 向き, スコア] を格納する

    direction_map = {0:[-1, 0], 1:[0, 1], 2:[1, 0], 3:[0, -1]}
    while not q.empty():
        curr_loc, curr_d, curr_score = q.get()
        curr_y, curr_x = curr_loc
        if scores[curr_y][curr_x][curr_d] < curr_score:
            continue

        for d in range(4):
            if curr_score + 1 < scores[curr_y][curr_x][d]:
                scores[curr_y][curr_x][d] = curr_score + 1
                q.put([curr_loc, d, curr_score+1])
                
        dy, dx = direction_map[curr_d]
        while(True):
            curr_x += dx
            curr_y += dy
            if (not 0 <= curr_x < W) or (not 0 <= curr_y < H):
                break
            if box[curr_y][curr_x] == "#":
                break
            if curr_score < scores[curr_y][curr_x][curr_d]:
                scores[curr_y][curr_x][curr_d] = curr_score
                q.put([(curr_y, curr_x), curr_d, curr_score])

    print(min(scores[t[0]][t[1]]))

solve()