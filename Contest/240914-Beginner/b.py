def solve():
    N, M = map(int, input().split())
    counter = [0 for _ in range(N)]

    for m in range(M):
        a, b  = input().split()
        a = int(a) - 1
        if b == "F":
            print("No")
            continue
        else:
            if counter[a] == 0:
                print("Yes")
            else:
                print("No")
            counter[a] = 1

solve()