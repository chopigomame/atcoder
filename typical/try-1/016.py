def get_inputs():
    N = int(input())
    A, B, C = map(int, input().split())
    return N, A, B, C





def solve():
    N, A, B, C = get_inputs()
    min_count = 10000
    for i in range(10000):
        for j in range(10000 - i):
            reside = (N - i * A - j * B)
            if reside < 0:
                break
            if reside % C == 0:
                k = reside // C
                min_count = min(i + j + k, min_count)

    print(min_count)

solve()