import itertools
import math

def prime_factorize(n):
    if n < 2:
        return {} 
    
    ret = {}
    for i in range(2, int(n ** 0.5) + 1):
        while(n % i == 0):
            ret.setdefault(i, 0)
            ret[i] += 1
            n //= i
    
    if n > 1:
        ret.setdefault(n, 0)
        ret[n] += 1
    return ret
            

def solve():
    K = int(input())
    primes = prime_factorize(K)
    if len(primes) == 0:
        print(1)
        return
    primes_keys = list(primes.keys())
    primes_values = list(primes.values())
    primes_orders_combination = [list(range(e+1)) for e in primes.values()]
    
    count = 0
    for orders in itertools.product(*primes_orders_combination):
        b_primes_orders_combination = [list(range(primes_values[i] - e + 1)) for i, e in enumerate(orders)]
        for b_orders in itertools.product(*b_primes_orders_combination):
            c_orders = [primes_values[i] - orders[i] - b_orders[i] for i, e in enumerate(b_orders)]
            a = math.prod([prime ** orders[i] for i, prime in enumerate(primes_keys)])
            b = math.prod([prime ** b_orders[i] for i, prime in enumerate(primes_keys)])
            c = math.prod([prime ** c_orders[i] for i, prime in enumerate(primes_keys)])
            if a <= b <= c:
                count += 1
    print(count)

solve()