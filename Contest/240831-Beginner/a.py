def get_inputs():
    A, B = map(int, input().split())
    return A, B


def solve():
    A, B = get_inputs()
    if A == B:
        return 1
    if (A - B) % 2 != 0:
        return 2
    return 3

print(solve())