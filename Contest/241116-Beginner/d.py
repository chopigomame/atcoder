import math
def get_inputs():
    S = input()
    Q = int(input())
    Ks = list(map(int, input().split()))
    return S, Q, Ks

def solve():
    S, Q, Ks = get_inputs()
    L = len(S)
    
    ans = []
    for k in Ks:
        k -= 1
        s = S[k % L]

        count = 0
        b = (k // L)
        while(True):
            if b == 0:
                if count %2 == 0:
                    ans.append(s)
                else:
                    ans.append(s.swapcase())
                break
            # exp = math.floor(math.log2(b))
            b -= 2 ** (b.bit_length() -1)
            count += 1

    
    print(*ans)

solve()