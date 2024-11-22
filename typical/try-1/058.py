def get_inputs():
    N, K = map(int, input().split())
    return N, K

def solve():
    x, K = get_inputs()
    got_dict = {}
    K_residue = 0
    for i in range(1, K+1): # detect loop
        y = 0
        for j in range(5):
            y += (x // (10 ** j)) % 10
        x = (x + y) % (10 ** 5)
        if x in got_dict:
            cycle = i - got_dict[x]
            K_residue = (K - got_dict[x]) % cycle # remove not-neecssary loop iterations
            break
        got_dict[x] = i
    
    for k in range(K_residue): # calc reside iters considering loops
        y = 0
        for i in range(5):
            y += (x // (10 ** i)) % 10
        x = (x + y) % 10 ** 5
    print(x)

solve()
        