import bisect
def get_inputs():
    N, M = map(int, input().split())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))
    return N, M, As, Bs

def solve():
    N, M, As, Bs = get_inputs()
    Bs_with_idx = sorted([[i, b] for i, b in enumerate(Bs)], key=lambda x:x[1])
    Bs_sorted = [e[1] for e in Bs_with_idx]

    ans = {b: -1 for b in range(M)}
    prev_idx = N
    start_idxes = []
    for i, a in enumerate(As):
        bisect_idx = bisect.bisect_left(Bs_sorted, a)
        if bisect_idx == N:
            continue
        start_idxes.append(bisect_idx)
        # for b_idx, _ in Bs_with_idx[bisect_idx:prev_idx]:
        #     if ans[b_idx] == -1:
        #         ans[b_idx] = i + 1
        # prev_idx = bisect_idx

    for j in range(M):
        
        print(ans[j])



solve()