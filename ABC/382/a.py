def solve():
    N, D = map(int, input().split())
    S = input()

    total_num = S.count("@")
    print(N - (total_num - D))

solve()
