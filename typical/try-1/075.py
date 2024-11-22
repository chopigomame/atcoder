from math import sqrt
def trial_division(n):
    if n < 2:
        return [n]

    prime_factors = []
    root_n = int(sqrt(n)) + 1
    for i in range(2, root_n):
        while n % i == 0:
            prime_factors.append(i)
            n //= i
    if n > 1:
        prime_factors.append(n)
            
    return prime_factors

def solve():
    N = int(input())
    pfs = trial_division(N)
    l = len(pfs)
    count = 0
    while(l > 1):
        l = l//2 + l%2
        count += 1
    print(count)

solve()