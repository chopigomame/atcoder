import bisect
def solve():
    N, K = map(int, input().split())
    S = input()

    alphabet_map = {e:[] for e in "abcdefghijklmnopqrstuvwxyz"}

    for i, s in enumerate(S):
        alphabet_map[s].append(i)

    ret_s = ""
    curr_idx = -1
    for k in range(K):
        reside = K - len(ret_s)
        for alpha in alphabet_map.keys():
            idx = bisect.bisect_right(alphabet_map[alpha], curr_idx)
            if idx == len(alphabet_map[alpha]):
                continue
            idx = alphabet_map[alpha][idx]
            if N - idx >= reside:
                ret_s += alpha
                curr_idx = idx
                break
    
    print(ret_s)

solve()
