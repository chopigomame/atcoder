def get_inputs():
    N, K = map(int, input().split())
    scores = []
    for _ in range(N):
        A, B = map(int, input().split())
        scores.append(B)
        scores.append(A-B)
    return N, K, scores

def solve():
    N, K, scores = get_inputs()
    scores.sort(reverse=True)
    print(sum(scores[:K]))

solve()