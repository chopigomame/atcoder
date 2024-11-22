def get_inputs():
    a, b, c = map(int, input().split())
    return a, b, c

def solve():
    a, b, c = get_inputs()
    if a < c**b:
        print("Yes")
    else:
        print("No")

solve()