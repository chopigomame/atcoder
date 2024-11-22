import bisect

def solve():
    N = int(input())
    users = []
    s1 = input()
    users.append(s1)
    print(1)
    for n in range(2, N+1):
        s = input()
        left_idx = bisect.bisect_left(users, s)
        if left_idx != len(users) and users[left_idx] == s:
            continue
        else:
            print(n)
            users.insert(left_idx, s)

solve()