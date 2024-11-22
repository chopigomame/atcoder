def solve():
    N = int(input())
    origAs = list(map(int, input().split()))

    ans = 0
    for s in [0, 1]:
        As = origAs[s:]
        l, r = 0, 0
        last_index = {e:-1 for e in As}
        length = len(As)

        for i in range(length):
            even = 2*i
            odd = 2*i + 1
            if odd >= length:
                ans = max(r - l + 1, ans)
                break

            if As[even] == As[odd]:
                A = As[odd]
                if last_index[A] >= l:
                    ans = max(r - l + 1, ans)
                    l = last_index[A] + 1

                r = odd
                last_index[A] = r
            else:
                ans = max(r - l + 1, ans)
                l, r = odd + 1, odd + 1
    
    if ans == 1:
        print(0)
    else:
        print(ans)

solve()
