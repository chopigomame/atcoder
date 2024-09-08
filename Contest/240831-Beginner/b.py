def solve():
    N = int(input())
    stress = 0
    first_l = True
    first_r = True
    for _ in range(N):
        a, s = input().split()
        a = int(a)
        if s == "L":
            if first_l:
                prev_l = a
                first_l = False
            else:
                stress += abs(prev_l - a)
                prev_l = a
        if s == "R":
            if first_r:
                prev_r = a
                first_r = False
            else:
                stress += abs(prev_r - a)
                prev_r = a
    print(stress)
solve()