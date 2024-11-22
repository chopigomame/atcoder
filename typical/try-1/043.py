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
    arriveds = {s}
    q = queue.Queue()
    q.put([s, 0]) # [位置、距離] を格納する

    while q:
        now, dist = q.get()
        for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_y = now[0] + dy
            next_x = now[1] + dx
            next = (next_y, next_x)
            if not 0 <= next_y < H or not 0 <= next_x < W:
                continue
            if box[next_y][next_x] != "#" and not next in arriveds:
                q.put([(next_y, next_x), dist + 1])
                arriveds.add(next)
            if next == t:
                print(dist + 1)
                return

solve()