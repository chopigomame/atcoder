import bisect
def get_inputs():
    N, M = map(int, input().split())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))
    return N, M, As, Bs

def solve():
    N, M, As, Bs = get_inputs()
    As_with_idx = sorted([[i, a] for i, a in enumerate(As)], key=lambda x:x[1])
    As_sorted = [e[1] for e in As_with_idx]

    for b in Bs:
        bisect_idx = bisect.bisect_left(As_sorted, b)
        if bisect_idx == 0 and As_sorted[0] > b:
            print(-1)
        elif bisect_idx == N:
            print(N-1)
        else:
            smaller_idx = max(0, bisect_idx - 1)
            larger_idx = bisect_idx
            if As_sorted[smaller_idx] <= b: # 一致があるとき
                print(As_with_idx[smaller_idx][0] + 1)
            else:
                print(As_with_idx[larger_idx][0] + 1)


solve()