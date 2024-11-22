def calc_z(x):
    _x = x
    y = 0
    for i in range(4, -1, -1):
        y += x//(10**i)
        x %= (10**i)
    z = (_x + y) % (10**5)
    return z

def solve():
    N, K = map(int, input().split())
    z = N
    iters = [-1 for _ in range(10**5)]
    iter = 0
    while(True):
        z = calc_z(z)
        iter += 1
        if iter == K:
            print(z)
            return
        if iters[z] != -1:
            cycle = iter - iters[z]
            break
        iters[z] = iter
    
    residue = (K - iter) % cycle
    for _ in range(residue):
        z = calc_z(z)
    print(z)
    
solve()