import math

def solve():
    A, B, C = map(int, input().split())

    d = math.gcd(A,B,C)

    print(A//d + B//d + C//d - 3)
    
solve()