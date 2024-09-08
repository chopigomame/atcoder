def get_inputs():
    L, R = map(int, input().split())
    return L, R

def solve():
    L, R = get_inputs()
    if L == 1 and R == 1 or L == 0 and R == 0:
        print("Invalid")
    elif L == 1:
        print("Yes")
    elif R == 1:
        print("No")
        
solve()