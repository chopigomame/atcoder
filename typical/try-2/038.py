import math
def solve():
    A, B = map(int, input().split())
    gcd = math.gcd(A, B)
    lcm = A * B // gcd

    if lcm > 10**18:
        print("Large")
    else:
        print(lcm)

solve()
