import itertools
def get_inputs():
    H, W = map(int, input().split())
    Ps = []
    for h in range(H):
        Ps.append(list(map(int, input().split())))
    return H, W, Ps

def solve():
    H, W, Ps = get_inputs()
    max_size =0
    for hs in itertools.product([0, 1], repeat=H):
        use_row_nums = [i for i in range(H) if hs[i]==1]
        if not use_row_nums:
            continue

        count = {}
        for w in range(W):
            if all([ Ps[j][w] == Ps[use_row_nums[0]][w] for j in use_row_nums]):
                count.setdefault(Ps[use_row_nums[0]][w], 0)
                count[Ps[use_row_nums[0]][w]] += 1
        if len(count) != 0:
            max_count = max(count.values())
            if max_count * len(use_row_nums) > max_size:
                max_size = max_count * len(use_row_nums)
    print(max_size)

solve()