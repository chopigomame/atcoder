import itertools
def get_inputs():
    H, W = map(int, input().split())
    Ps = []
    for _ in range(H):
        p = list(map(int, input().split()))
        Ps.append(p)
    return H, W, Ps

def solve():
    H, W, Ps = get_inputs()
    max_size_candidates = [0 for _ in range(2**H)]
    for i, h_pair in enumerate(itertools.product([0, 1], repeat=H)):
        columns = [0 for _ in range(H*W + 1)]
        active_rows_num = sum(h_pair)
        if active_rows_num == 0:
            continue
        for w in range(W):
            nums = [Ps[h][w] for h, b in enumerate(h_pair) if b == 1]
            num = nums[0]
            if all([e == num for e in nums]):
                columns[num] += 1
        max_size_candidates[i] = max(columns) * active_rows_num
    
    print(max(max_size_candidates))

solve()
    
        