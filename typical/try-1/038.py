import math
def solve():
    A, B = map(int, input().split())
    c = math.gcd(A, B)
    ans = A * B // c
    if ans <= 10 ** 18:
        print(ans)
    else:
        print("Large")

solve()