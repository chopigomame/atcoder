def get_inputs():
    N, Q = map(int, input().split())
    As = list(map(int, input().split()))
    return N, Q, As

def solve():
    def convert_idx(idx):
        return (start_idx + idx)%N
    
    N, Q, As = get_inputs()
    start_idx = 0
    count2 = 0
    for q in range(Q):
        T, x, y = map(int, input().split())
        x -= 1; y -= 1
        if T == 1:
            x, y = convert_idx(x), convert_idx(y)
            As[x], As[y] = As[y], As[x]
        if T == 2:
            count2 += 1
            start_idx = (N-count2) % N
        if T == 3:
            print(As[convert_idx(x)])

solve()
              