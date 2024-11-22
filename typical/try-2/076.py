import bisect
def solve():
    N = int(input())
    As = list(map(int, input().split()))

    accums = []
    accum = 0
    for a in As:
        accum += a
        accums.append(accum)
    total = accums[-1]
    if total % 10 != 0:
        print("No")
        return

    for a in accums[:N]:
        accums.append(total + a)

    for a in accums:
        want = a - total//10
        i = bisect.bisect_left(accums, want)
        if accums[i] == want:
            print("Yes")
            return
    print("No")
    return

solve()