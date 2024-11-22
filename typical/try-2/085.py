import math
import itertools
def prime_factorize(n):
    if n == 2:
        return {2:1}

    i = 2
    factors = {}
    while(True):
        while(n % i == 0):
            factors.setdefault(i, 0)
            factors[i] += 1
            n //= i
        i += 1
        if i > n:
            break
    if n != 1:
        factors[n] = 1
    
    return factors

def solve():
    K = int(input())
    prime_factors = prime_factorize(K)
    factors = list(prime_factors.keys())
    factor_nums = [prime_factors[k] for k in factors]
    N = len(factors)

    count = 0
    for factor_nums_a in itertools.product(*[range(n+1) for n in factor_nums]):
        for factor_nums_b in itertools.product(
            *[range(factor_nums[i] - n + 1) for i, n in enumerate(factor_nums_a)]):
            
            a = math.prod([factors[i] ** factor_nums_a[i] for i in range(N)])
            b = math.prod([factors[i] ** factor_nums_b[i] for i in range(N)])
            if b < a:
                continue
            c = K / a / b
            if c < b:
                continue
            count += 1
    
    print(count)

solve()