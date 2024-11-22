import math
def get_inputs():
    T = int(input())
    L, X, Y = map(int, input().split())
    Q = int(input())
    return T, L, X, Y, Q

def solve():
    T, L, X, Y, Q = get_inputs()
    for q in range(Q):
        E = int(input())
        kanran_theta = -(math.pi / 2) - 2 * math.pi * E/T
        y = L/2 * math.cos(kanran_theta)
        z = L/2 * math.sin(kanran_theta) + L/2
        theta = math.atan(z / math.sqrt((Y-y)**2 + X**2))
        print(math.degrees(theta))

solve()