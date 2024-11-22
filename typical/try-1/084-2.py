def solve():
    N = int(input())
    S = input()
    
    idx_memos = {"o": [], "x": []}
    for i, s in enumerate(S):
        idx_memos[s].append(i)

    lookable_idxes = {s: 0 for s in ["o", "x"]}
    correspondences = {"o": "x", "x": "o"}
    count = 0
    for i, s in enumerate(S):
        correspondence = correspondences[s]
        idx_memos_correspondence = idx_memos[correspondence]
        lookable_idx_correspondence = lookable_idxes[correspondence]
        if lookable_idx_correspondence >= len(idx_memos_correspondence):
            continue

        absolute_correspondence_idx = idx_memos_correspondence[lookable_idx_correspondence]
        count += N - absolute_correspondence_idx
        
        lookable_idxes[s] += 1
    print(count)

solve()